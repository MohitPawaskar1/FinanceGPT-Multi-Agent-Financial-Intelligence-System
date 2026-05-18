from fastapi import APIRouter

from pydantic import BaseModel

from app.orchestration.workflow import (
    build_workflow
)


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


class AnalysisRequest(
    BaseModel
):

    file_path: str


@router.post("/run")
def run_analysis(
    request: AnalysisRequest
):

    workflow = build_workflow()

    state = {

        "file_path":
        request.file_path,

        "user_query":
        "Analyze financial performance"
    }

    result = workflow.invoke(state)

    return {

        "insights":
        str(result.get("insights", "")),

        "commentary":
        str(result.get("commentary", "")),

        "forecast_summary":
        str(
            result.get(
                "forecast_summary",
                ""
            )
        ),

        "anomaly_summary":
        str(
            result.get(
                "anomaly_summary",
                ""
            )
        )
    }