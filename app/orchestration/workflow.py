from langgraph.graph import (
    StateGraph
)

from app.orchestration.state import (
    FinanceState
)

from app.orchestration.intent_router import (
    determine_route
)

from app.orchestration.nodes import (
    ingestion_node,
    insight_node,
    forecast_node,
    anomaly_node,
    rag_query_node
)


def build_workflow():

    workflow = StateGraph(
        FinanceState
    )

    workflow.add_node(
        "ingestion",
        ingestion_node
    )

    workflow.add_node(
        "insight",
        insight_node
    )

    workflow.add_node(
        "forecast",
        forecast_node
    )

    workflow.add_node(
        "anomaly",
        anomaly_node
    )

    workflow.add_node(
        "query",
        rag_query_node
    )

    workflow.set_entry_point(
        "ingestion"
    )

    workflow.add_conditional_edges(
        "ingestion",
        determine_route,
        {
            "forecast": "forecast",
            "anomaly": "anomaly",
            "query": "query",
            "insight": "insight"
        }
    )

    workflow.set_finish_point(
        "forecast"
    )

    workflow.set_finish_point(
        "anomaly"
    )

    workflow.set_finish_point(
        "query"
    )

    workflow.set_finish_point(
        "insight"
    )

    return workflow.compile()