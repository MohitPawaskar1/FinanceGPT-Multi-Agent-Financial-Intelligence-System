from langchain_core.documents import Document

from app.rag.chroma_manager import (
    get_vector_store
)


def ingest_financial_analysis(
    insights,
    commentary
):

    vector_store = get_vector_store()

    documents = [

        Document(
            page_content=insights,
            metadata={
                "type": "insights"
            }
        ),

        Document(
            page_content=commentary,
            metadata={
                "type": "commentary"
            }
        )
    ]

    vector_store.add_documents(documents)

    print("\nData successfully stored in ChromaDB.")