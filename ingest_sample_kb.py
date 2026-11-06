##  Create a simple script that loads the sample documents, chunks them, and uploads them into Pinecone.                   

from pathlib import Path
from app.core.config import get_settings
settings=get_settings()
from app.services.ingestion import load_file, chunk_documents
from app.rag.vectorstore import add_documents

## The data placed within the .md files within:- "data\\sample_kb":-:-:_:_:_:_:-:-.,;;    
## We had already mentioned the above path within the config.py file using the tag:- sample_kb_dir:-.,;;
folder = Path(settings.sample_kb_dir)
# for file in folder
files = [p for p in folder.iterdir() if p.is_file()]
##  we will go through the above files list.,;; and will chunk the data accordingly,..!!..,,;;,:-:-:_:_:-:-:_:_.,;;\\//  ~~>> and store within the vector db..!!..,,;;
all_docs=[]
for path in files:
    all_docs.extend(load_file(path))
chunks = chunk_documents(all_docs)
ids = add_documents(chunks)
print(f"Indexed {len(files)} files -> {len(chunks)} chunks -> {len(ids)} Pinecone vector db.")