from app.core.llm import get_llm

from app.rag.retriever import (
    retrieve_relevant_context
)

from app.prompts.rag_prompt import (
    RAG_PROMPT
)


def generate_rag_response(query):

    llm = get_llm()

    retrieved_docs = retrieve_relevant_context(
        query
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    prompt = RAG_PROMPT.format(
        context=context,
        query=query
    )

    response = llm.invoke(prompt)

    return response.content