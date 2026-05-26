from fastapi import APIRouter

from pydantic import BaseModel

from app.data.loader import (
    load_financial_data
)

from app.query_engine.agent import (
    answer_financial_query
)


router = APIRouter()


# =========================================
# REQUEST MODEL
# =========================================

class QueryRequest(BaseModel):

    query: str

    file_path: str


# =========================================
# QUERY ROUTE
# =========================================

@router.post("/query/run")

def run_query(
    request: QueryRequest
):

    try:

        # =================================
        # LOAD DATASET
        # =================================

        df = load_financial_data(
            request.file_path
        )

        # =================================
        # GENERATE RESPONSE
        # =================================

        response = (
            answer_financial_query(

                request.query,

                df
            )
        )

        return {

            "response":
            str(response)
        }

    except Exception as e:

        return {

            "response":
            f"Query processing failed: {str(e)}"
        }