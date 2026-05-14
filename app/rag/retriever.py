from app.rag.chroma_manager import (
    get_vector_store
)


def retrieve_relevant_context(query):

    vector_store = get_vector_store()

    results = vector_store.similarity_search(
        query,
        k=3
    )

    return results