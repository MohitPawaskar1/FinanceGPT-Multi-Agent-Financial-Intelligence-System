from app.core.llm import get_llm

from app.orchestration.prompts import (
    INTENT_ROUTER_PROMPT
)


def determine_route(state):

    llm = get_llm()

    query = state["user_query"]

    prompt = INTENT_ROUTER_PROMPT.format(
        query=query
    )

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    allowed_routes = [
        "forecast",
        "anomaly",
        "query",
        "insight"
    ]

    if route not in allowed_routes:

        route = "insight"

    return route