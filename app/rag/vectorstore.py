import time
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from app.core.config import get_settings
settings=get_settings()


_embeddings=None
_vectorstore=None

##  list of possible embedding models to choose from; basically if the end user decides to change the embedding models from the backend; from those cases;; we are also mentioning//or// providing the respective dimensions for them..!!..,,;;::__:_:_;;;;::--:-:-.,;;
EMBEDDING_DIMENSIONS = {
    "text-embedding-3-small":1536,
    "text-embedding-3-large":3072,
    "text-embedding-ada-002": 1536,
    "all-minilm-l6-v2": 384,
}


##  takes the model name, and, returns the respective dimensions:-:-:_:_.,;;.,;;
def get_embedding_dimension(model_name: str | None = None) -> int:
    name = (model_name or settings.embedding_model or "").strip()
    if not name:
        raise RuntimeError("Embedding model is not configured..!!..,,;;")


    normalized=name.lower()
    if normalized in EMBEDDING_DIMENSIONS:
        return EMBEDDING_DIMENSIONS[normalized]
    if "text-embedding-3-small" in normalized:
        return 1536
    if "text-embedding-3-large" in normalized:
            return 3072
    if "text-embedding-ada-002" in normalized:
            return 1536
    if "all-minilm-l6-v2" in normalized:
            return 384

    raise ValueError(
          f"Unsupported embedding model '{model_name or settings.embedding_model}' for Pinecone....,,,,.,;;;;;;"
          "Add the matching dimension to EMBEDDING_DIMENSIONS."
    )



## Loading or getting the embedding models.,;;..!!!!...,;;
def get_embeddings():
      ##  Making the variable as global..!!..,,;;
      global _embeddings
      ##  Since this variable is defined as None above.,;; this condition will satisfy..!!!!..,,;;
      if _embeddings is None:
            ##  Next it checks if openai api key is there or not.,;; if not there then raise error else.,;; get it..!!!!..,,;;
            if not settings.openai_api_key:
                  raise RuntimeError("OPENAI_API_KEY is missing....,,,,;;;;;;;;")
            _embeddings = OpenAIEmbeddings(
                  model=settings.embedding_model,
                  api_key=settings.openai_api_key,
            )
      return _embeddings   

##   PineCone index creations:-:_:-:_.,;;.,;;.,;;.,;;\\\\||||
def ensure_index():
    if not settings.pinecone_api_key:
        raise RuntimeError("PINECONE_API_KEY is missing")

    ##  Initially getting the dimensions from the above functions' mappings..!!..,,;;
    desired_dimension = get_embedding_dimension()
    ## Initializing the pinecone:-:-:_:_:-:-:_:_.,;;.,;;.,;;.,;;
    pc = Pinecone(api_key=settings.pinecone_api_key)
    ## Checking by getting the list of available indexes..!!..,,;;..!!..,,;;
    names = [x["name"] for x in pc.list_indexes()]

    ## Checking if our index name is already present or there within the list of indexes..!!..,,;; -->> Only then we will proceed with the following functionalities..!!..,,;;;;;;
    if settings.pinecone_index_name in names:
        index_info = pc.describe_index(settings.pinecone_index_name)
        current_dimension = getattr(index_info, "dimension", None)
        if current_dimension is None and isinstance(index_info, dict):
            current_dimension = index_info.get("dimension")

        if current_dimension is not None and current_dimension != desired_dimension:
            pc.delete_index(name=settings.pinecone_index_name)
            while settings.pinecone_index_name in [x["name"] for x in pc.list_indexes()]:
                time.sleep(1)

    ## Else if the given index name is not there //or// present within our//the list of indexes.,;; then we will be creating a new one..!!..,,;;
    if settings.pinecone_index_name not in [x["name"] for x in pc.list_indexes()]:
        pc.create_index(
            name=settings.pinecone_index_name,
            dimension=desired_dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(settings.pinecone_index_name).status["ready"]:
            time.sleep(1)

    return pc.Index(settings.pinecone_index_name)

## Storing our vectors /(embeddings) within the vector db:-:-:_:_.,;;.,;;:-:-:_:_.,;;.,;;.,;;.,;;.,;;.,;;\\\\
## >> creation of the namespace:=:-:_:_.,;;
def get_vectorstore():
     global _vectorstore
     if _vectorstore is None:
          index = ensure_index()
          _vectorstore = PineconeVectorStore(
               index=index,
               embedding=get_embeddings(),
               namespace=settings.pinecone_namespace,
          )
     return _vectorstore

## >> getting the retrievers:-:_:-:_.,;;.,;;.,;;.,;;....,,,,;;;;;;;;
def get_retriever():
     return get_vectorstore().as_retriever(search_kwargs={"k":settings.top_k})



## >>  adding the docyuments:-:-:_:_.,;;.,;;
def add_documents(chunks):
     store=get_vectorstore()
     return store.add_documents(chunks)

