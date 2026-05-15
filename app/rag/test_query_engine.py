from app.rag.query_engine import (
    generate_rag_response
)


def test_query_engine():

    query = (
        "What financial trends indicate "
        "strong business growth?"
    )

    response = generate_rag_response(
        query
    )

    print("\nRAG RESPONSE:\n")

    print(response)


if __name__ == "__main__":
    test_query_engine()