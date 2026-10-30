## used especially for production grade projects or/or applications..!!..,,;;

from functools import lru_cache ## used for or within config files especially.,;;..!!..,,;;
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2] ##  so that it directs to the base directory everytime while runnings..!!..,,;;

# Pydantic Settings ..!!..,,;;:_:_:-:-
##  ~~>>  maintains that these changes or data gets maintained..!!..,,;;
class Settings(BaseSettings):
    app_name : str = "Enterprise IT Support Agentic RAG Copilot"
    app_env: str = "development"
    openai_api_key: str = ""
    groq_api_key: str = ""
    tavily_api_key: str = ""
    pinecone_api_key: str = ""    
    pinecone_index_name: str = "fde-it-support-rag"
    pinecone_namespace: str = "company-it-kb"
    embedding_model : str = "text-embedding-3-small"
    openai_model: str = "gpt-4o-mini"
    groq_model: str = "gpt-4o-mini"
    groq_model: str = "openai/gpt-oss-20b"
    top_k: int = 4
    max_retries: int = 2
    admin_api_key: str = "change-me"  ## dummy password that can be used within our UI..!!..,,;;
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    ##  stores the audit.db file (using postgresql) within the existing data folders..!!..,,;;
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"), extra="ignore")
    ##  ~~>> for the above mentioned fields like :- "openai_api_key", etc.,;;//or//others.,;;  which fields are not given needs to be picked from the .env files..!!..,,;;


@lru_cache
def get_settings() -> Settings:
    return Settings()
## ~~>> returning the settings class..!!..,;;    