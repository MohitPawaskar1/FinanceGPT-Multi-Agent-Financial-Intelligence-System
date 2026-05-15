from fastapi import APIRouter

from app.orchestration.workflow import (
    build_workflow
)


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


@router.post("/run")
def run_analysis():

    workflow = build_workflow()

    state = {

        "file_path":
        "datasets/sample_financial_data.csv",

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