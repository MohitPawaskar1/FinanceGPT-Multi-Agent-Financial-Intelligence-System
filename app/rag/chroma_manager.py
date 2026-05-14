from langchain_chroma import Chroma

from app.rag.embeddings import (
    get_embedding_function
)


CHROMA_DB_DIR = "app/database/chroma_db"

COLLECTION_NAME = "financial_memory"


def get_vector_store():

    embeddings = get_embedding_function()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    return vector_store