"""Read-only disk-backed legal search helper; standard library only."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sqlite3
import unicodedata

STOP=set('der die das ein eine einer einem einen des den dem und oder von vom zu zur zum auf an im in ist sind mit nach für als auch nicht sich es sie er bei aus über durch dass wird werden können kann sowie'.split())

def open_index(path):
    c=sqlite3.connect(Path(path).resolve().as_uri()+'?mode=ro&immutable=1',uri=True)
    c.execute('pragma cache_size=-65536');c.execute('pragma temp_store=FILE');c.execute('pragma query_only=ON')
    return c

def tokens(text):
    # Match FTS5 unicode61's diacritic removal for term-frequency lookup.
    s=''.join(x for x in unicodedata.normalize('NFD',text.lower()) if unicodedata.category(x)!='Mn')
    return [x for x in dict.fromkeys(re.findall(r'[^\W_]+',s)) if len(x)>=3 and x not in STOP and not x.isdigit()]

def terms(c,text,n=12):
    scored=[]
    for pos,t in enumerate(tokens(text)):
        row=c.execute('select doc from vocabulary where term=?',(t,)).fetchone()
        if row and 2<=row[0]<=300000:scored.append((row[0],pos,t))
    return [t for _,_,t in sorted(scored)[:n]]

def search(c,text,k=200,variant='text'):
    ts=terms(c,text,12)
    if not ts:return []
    expr=' OR '.join('"'+t+'"' for t in ts)
    weights={'text':(1,1,1),'title':(8,8,1),'focused':(8,2,1)}[variant]
    if variant=='focused':expr=' OR '.join('"'+t+'"' for t in ts[:6])
    rows=c.execute('select d.citation,search.rank from search join documents d on d.doc_id=search.rowid where search match ? and rank match ? order by rank limit ?',
                   (expr,'bm25('+','.join(map(str,weights))+')',k)).fetchall()
    # SQLite's BM25 order is deterministic for a frozen index; final equal-score ties use the ID.
    return sorted(rows,key=lambda x:(x[1],x[0]))

def extract(c,text):
    patterns=[r'Art\.\s*\d+[a-z]*(?:\s+Abs\.\s*\d+[a-z]*)?\s+[A-Z][A-Za-zÜüÖöÄä0-9.]*',
              r'BGE\s+\d+\s+[IVX]+[a-z]?\s+\d+(?:\s+E\.?\s*\d+[a-z]*(?:\.\d+[a-z]*)*)?']
    out=[]
    for pat in patterns:
        for m in re.finditer(pat,text):
            cit=' '.join(m[0].split())
            if c.execute('select 1 from documents where citation=?',(cit,)).fetchone() and cit not in out:out.append(cit)
    return out

def document(c,citation):
    rows=c.execute('''select s.source_file,s.file_row,s.citation,s.title,t.text,t.text_id
      from documents d join document_members m on m.doc_id=d.doc_id join source_rows s on s.source_row=m.source_row
      join texts t on t.text_id=s.text_id where d.citation=? order by s.source_row''',(citation,)).fetchall()
    seen=set();texts=[]
    for r in rows:
        if r[-1] not in seen:seen.add(r[-1]);texts.append(r[-2])
    return {'citation':citation,'text':'\n'.join(texts),'members':[{'source_file':r[0],'file_row':r[1],'citation':r[2]} for r in rows]}

def main():
    p=argparse.ArgumentParser();p.add_argument('--index',default=str(Path(__file__).with_name('corpus.sqlite')))
    p.add_argument('--query');p.add_argument('--citation');p.add_argument('--k',type=int,default=10)
    a=p.parse_args();c=open_index(a.index)
    print(json.dumps(document(c,a.citation) if a.citation else search(c,a.query or '',a.k),ensure_ascii=False))

if __name__=='__main__':main()
