## in order to Create FASTAPI endpoints for chatting with the Agentic RAG system, uploading documents, health checks, and audit informations.
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, Header
from pydantic import BaseModel, Field
from app.core.config import get_settings
from app.rag.workflow import ask  ## for the state
from app.rag.vectorstore import add_documents  ## adding the documents within our knwoledge bases..!!..,,;;
from app.services.ingestion import load_file, chunk_documents, SUPPORTED ## data ingestion capabilities..  ~~>>  whenever user uplaods a new doc; and we need to store within the kb using the above. ..!!..,,;;
from app.services.audit import write_audit  ## storing the logs within the db. ..!!..,,;;

router = APIRouter(prefix="/api")  ## needs to be used while creating the api route..!!..,,;;
settings = get_settings()
class ChatRequest(BaseModel): ##Pydantic models.,;;
    question: str = Field(min_length=2, max_length=3000)  ## validator to accept the question size from the end user


## this basically checks the health of the application. by calling the api router and getting the uinformation, using "get"..!!..,,;;
@router.get("/health")
def health():
    return {"status":"ok", "service":settings.app_name}    


@router.post("/chat")  ## since we are getting the information or question or request from the end users;; hence we mention the "post" requests..!!..,,;;
def chat(payload: ChatRequest): ## using this pydantic class named as ChatRequest, since we are expecting to get an / a question form the end users.
    try:#
        # pass
        # we are getting the answer; and have named it as "result"
        result = ask(payload.question)
        write_audit(payload.question, result["source_used"], result.get("trace",[]))
        # write_audit(payload.question, result["source_used"], result.get("trace", []))

        return{
            "answer":result["answer"],
            "source_used": result["source_used"],
            "trace": result.get("trace", []),
            "citations": result.get("citations", []),
            "rewritten_query": result.get("current_query", payload.question),
        }
    except Exception as exc:#
        raise HTTPException(status_code=500, detail=str(exc)) from exc#

## for the data ingestion parts..!!..,,;;..!!..,,;;:-:-:_:_:-:-:_:_.,;;.,;;.,;;.,;;
####  ``````-> ASYNC FUNCTIONS;;
@router.post("/ingest")  ## POST request as it takes documents from the end users..!!...,,;;.
async def ingest(file: UploadFile = File(...), x_admin_key: str = Header(default="")):  ## admin_key is used;; so that only the admin can ingest the newer documents..!!..,,;;
    if x_admin_key != settings.admin_api_key:
        ## If the admin_key does not match; we do not do anything..!!..,,;;....
        raise HTTPException(status_code=401, detail="Invalid admin key")
    ##else; we take in the file and and store it within the upload_dir or upload directory  ..!!..,,;;  
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in SUPPORTED:
        raise HTTPException(status_code=400, detail=f"Supported: {', '.join(sorted(SUPPORTED))}")
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest = upload_dir / Path(file.filename).name
    dest.write_bytes(await file.read())
    ## loading the files
    docs = load_file(dest)
    ## creating the chunks
    chunks = chunk_documents(docs)
    ids = add_documents(chunks)
    return {"message": "Document indexed", "file": dest.name, "chunks":len(chunks), "ids_created": len(ids)}


