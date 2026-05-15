from fastapi import (
    APIRouter
)

from pydantic import BaseModel

from app.rag.query_engine import (
    generate_rag_response
)


router = APIRouter(
    prefix="/query",
    tags=["RAG Query"]
)


class QueryRequest(BaseModel):

    query: str


@router.post("/run")
def run_query(
    request: QueryRequest
):

    response = generate_rag_response(
        request.query
    )

    return {
        "response": response
    }