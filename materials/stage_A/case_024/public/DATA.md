# Local legal retrieval data

train.csv and validation.csv: query_id,query,gold_citations (semicolon-separated).
test.csv: query_id,query. sample_submission.csv: query_id,predicted_citations.
The population is 1,064 original training queries with complete corpus coverage;
all original reference citations are retained. The supplied split keeps related
questions in one partition. The source ten English validation questions are not
part of this benchmark. Training languages are retained without translation.

corpus.sqlite is a shared read-only SQLite FTS5 database containing every source
row from laws_de.csv (175,933) and court_considerations.csv (2,476,315). Connect
with sqlite3.connect('file:corpus.sqlite?mode=ro&immutable=1', uri=True).
Tables: texts(text_id,digest,text); source_rows(source_row,source_file,file_row,
citation,canonical_citation,title,text_id,alias_citation,alias_kind);
documents(doc_id,citation,kind); aliases(citation,kind);
document_members(doc_id,source_row). source_row and one-based file_row preserve
all original records and original citation strings. texts deduplicates identical
texts only, preserving their first source occurrence. A document concatenates
its distinct texts in source-row order. Article bundles group existing paragraphs
under Art. N BOOK. BGE case bundles group existing considerations under
BGE volume section page. Numeric statute identifiers are never translated into
abbreviations. These bundles are additional retrieval documents, not matching
synonyms. No query-to-gold links or scoring rules are stored in the database.

search is a contentless FTS5 table with citation,title,text, using unicode61 with
diacritics removal. Join search.rowid to documents.doc_id. vocabulary is its
fts5vocab row table (term,doc,cnt). Use search MATCH with ORDER BY rank LIMIT k.
Full source text is accessed through document_members/source_rows/texts;
search.py exposes a read-only query command and a --citation document command.
It never downloads data or loads the full corpus into RAM.

Source attribution: train queries adapted from LEXam: Benchmarking Legal Reasoning
on 340 Law Exams (Fan et al., 2025), CC BY 4.0,
https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question .
LEXam authors: Yu Fan, Jingwei Ni, Jakob Merane, Yang Tian, Yoan Hermstrüwer,
Yinya Huang, Mubashara Akhtar, Etienne Salimbeni, Florian Geering, Oliver Dreyer,
Daniel Brunner, Markus Leippold, Mrinmaya Sachan, Alexander Stremitzer,
Christoph Engel, Elliott Ash, Joel Niklaus. Source organizer extracted citations
from answers; this reconstruction filters complete references, groups/splits
questions and adds source-derived corpus bundles. No endorsement implied.
The organizer describes corpus excerpts as Swiss official enactments/decisions
provided for research/competition without completeness or officialness guarantees.
The supplied competition access terms restrict use to noncommercial/academic
research. This local package does not grant wider redistribution permission.
