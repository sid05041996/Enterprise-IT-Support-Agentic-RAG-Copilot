from typing import List, Literal, Optional
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langchain_core.documents import Document

## Pydantic class which determines; if the flow needs to be sent to the kb or direct?..!!..,,;;
class RouteDecision(BaseModel):
    route: Literal["kb","direct"] = Field(
        description="Use kb foor questions needing Agentic RAG docs; direct for greetings/simple chats."
    )

## Pydantic class for Evidence Gradings..!!..,,;;..!!..,,;;
class EvidenceGrade(BaseModel):
    grade: Literal["good","weak"] = Field(
        description="good means evidence can answer the question; weak means not enough evidences."
    )
## state:-.,;;
class AgentState(TypedDict):
    question: str
    current_query: str
    kb_docs: List[Document]
    web_results: str
    kb_grade:str
    web_grade:str
    answer:str
    source_used:str
    retry_count:str
    trace:List[str]
    citations: List[dict]