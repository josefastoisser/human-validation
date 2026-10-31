# Conditional surface-sampling protocol

sample_count: 500000

seed_literal: 0

hash_input_serialization: M || DOMAIN || struct.pack(">QB", i, c), with no newline, length field, filename, JSON, prehash substitution or implicit encoding. M is exact original OBJ bytes. DOMAIN is the literal byte string given below; i is unsigned 64-bit big-endian; c is one unsigned byte.

domain_python_repr: b'\x00P16.sample500k.v1\x00seed=0\x00'

domain_hex: 005031362e73616d706c653530306b2e763100736565643d3000

digest: SHA256

uniform: k=int.from_bytes(digest[:8],big); u=(2*k+1)/2**65, equivalently (k+0.5)/2**64; correctly rounded once to binary64 using Python integer division

draw_indices: 0..499999

channels: {"0": "triangle area CDF", "1": "barycentric sqrt variate", "2": "barycentric split variate"}

prefix_optimization: hashlib.sha256 of M||DOMAIN is copied before appending each fixed-width >QB suffix; mathematically hashes full M bytes, not SHA256(M)

triangulation: Face order and vertex order preserved. Fan triangles (v0,vj,vj+1), j=1..n-2. Zero-area fans discarded only from sampling view; all stored vertices remain in A. Negative OBJ indices resolve relative to vertices available at face line; positive indices resolve to original vertex list.

cdf: Triangle areas are binary64 cross-product norms /2. Positive triangles remain in fan order. np.cumsum float64; normalize by last cumulative value; last CDF exactly 1. np.searchsorted side=right; a binary64 u rounded to 1 selects final positive triangle.

barycentric: (1-sqrt(u1),sqrt(u1)*(1-u2),sqrt(u1)*u2); interpolate original triangle vertices in float64 before applying the frozen rigid transform.

cache: Reference clouds are generated once from exact corrected mesh bytes, frozen with file/point hashes and sampler-source hash, and reused for all systems. Missing/tampered caches are errors, never silently regenerated during grading.

point_hash: SHA256 of C-order little-endian float64 XYZ bytes; 500000x3. File also hashed separately.
