"""Shared deterministic geometry reconstruction; no external OBJ assets are loaded."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[key]='2'
from array import array
import hashlib
import itertools
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from threadpoolctl import threadpool_limits

N_POINTS=16384
SEED=2026
MAX_VERTICES=2000000
MAX_FACES=4000000

class Invalid(ValueError):pass

def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()

def load_obj(path,limits=True):
    vertices=array('d');faces=array('q')
    with Path(path).open(encoding='utf-8',errors='strict') as f:
        for line in f:
            s=line.split('#',1)[0].split()
            if not s:continue
            if s[0]=='v':
                if len(s) not in [4,7]:raise Invalid('Vertex needs XYZ, optionally followed by RGB')
                try:vertices.extend(map(float,s[1:4]))
                except ValueError:raise Invalid('Invalid vertex')
                if limits and len(vertices)//3>MAX_VERTICES:raise Invalid('Vertex limit')
            elif s[0]=='f':
                if len(s)!=4:raise Invalid('Faces must be triangles')
                try:
                    for part in s[1:]:
                        fields=part.split('/')
                        if len(fields)>3 or not fields[0] or any(x and not x.lstrip('-').isdigit() for x in fields):raise ValueError()
                        v=int(fields[0]);faces.append(v-1 if v>0 else len(vertices)//3+v if v<0 else -1)
                except ValueError:raise Invalid('Invalid face index')
                if limits and len(faces)//3>MAX_FACES:raise Invalid('Face limit')
            elif s[0] not in ['vn','vt','o','g','s','mtllib','usemtl']:
                raise Invalid('Unsupported OBJ statement: '+s[0])
            # Normals/UVs/groups/material declarations are ignored, never loaded.
    v=np.asarray(vertices,dtype=np.float64).reshape(-1,3);f=np.asarray(faces,dtype=np.int64).reshape(-1,3)
    if not len(v) or not len(f) or not np.isfinite(v).all():raise Invalid('Empty or nonfinite mesh')
    if f.min()<0 or f.max()>=len(v):raise Invalid('Face index out of range')
    tri=v[f];areas=np.linalg.norm(np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]),axis=1)*.5
    if not np.isfinite(areas).all() or areas.sum()<=0:raise Invalid('Degenerate or invalid triangular face')
    return v,f,areas

def sample_surface(mesh,object_id):
    v,f,areas=mesh;rng=np.random.Generator(np.random.PCG64(SEED+int(object_id)))
    which=rng.choice(len(f),size=N_POINTS,p=areas/areas.sum())
    uv=rng.random((N_POINTS,2));a=np.sqrt(uv[:,0]);b=uv[:,1]
    tri=v[f[which]]
    points=(1-a[:,None])*tri[:,0]+(a*(1-b))[:,None]*tri[:,1]+(a*b)[:,None]*tri[:,2]
    if not np.isfinite(points).all():raise Invalid('Nonfinite sampled surface')
    return points

def center(points):
    q=np.array(points,dtype=np.float64,copy=True);q-=q.mean(axis=0)
    radius=float(np.sqrt(np.mean(np.sum(q*q,axis=1))))
    if not np.isfinite(radius) or radius<=0:raise Invalid('Zero or nonfinite RMS radius')
    return q,radius

def point_sha(points):return hashlib.sha256(np.asarray(points,dtype='<f8').tobytes(order='C')).hexdigest()

def primitive(axes,kind='ellipsoid',rings=16,segments=32):
    """Closed low-poly superellipsoid; axis half-lengths in millimeters."""
    exponent=1. if kind=='ellipsoid' else .5 if kind=='boxy' else 1.5
    signed=lambda x:np.sign(x)*np.abs(x)**exponent
    v=[[0.,0.,-float(axes[2])]]
    for j in range(1,rings):
        phi=-np.pi/2+np.pi*j/rings
        for i in range(segments):
            theta=2*np.pi*i/segments
            v.append([axes[0]*signed(np.cos(phi))*signed(np.cos(theta)),axes[1]*signed(np.cos(phi))*signed(np.sin(theta)),axes[2]*signed(np.sin(phi))])
    top=len(v);v.append([0.,0.,float(axes[2])]);f=[]
    for i in range(segments):f.append([0,1+(i+1)%segments,1+i])
    for j in range(rings-2):
        for i in range(segments):
            a=1+j*segments+i;b=1+j*segments+(i+1)%segments;c=a+segments;d=b+segments
            f.extend([[a,b,c],[b,d,c]])
    for i in range(segments):f.append([top,1+(rings-2)*segments+i,1+(rings-2)*segments+(i+1)%segments])
    return np.array(v),np.array(f)

def write_obj(path,v,f):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as stream:
        for p in v:stream.write('v '+' '.join(format(float(x),'.12g') for x in p)+'\n')
        for t in f:stream.write('f '+' '.join(str(int(i)+1) for i in t)+'\n')
