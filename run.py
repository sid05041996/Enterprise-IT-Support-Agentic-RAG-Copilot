# from app.core.config import get_settings

# settings=get_settings()

# print(f"App Name : {settings.app_name}")
# print(f"App Environment: {settings.app_env}")
# ## Similarly you can display almost all of the fields that we//or/or//you have mentioned .,;;    within the Pydantic Class of the Config files..!!..,,;;


# from app.services.ingestion import load_file, chunk_documents
# from pathlib import Path
# from app.rag.vectorstore import get_embeddings, ensure_index, add_documents

# docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
# chunks = chunk_documents(docs) ##docs

# print(len(chunks))##docs

# add_documents(chunks)

import uvicorn

if __name__ == "__main__":
    ## since the main.py file is within the app folders..!!..,,;;
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)