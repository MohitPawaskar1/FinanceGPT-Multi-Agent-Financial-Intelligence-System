def determine_route(state):

    user_query = (
        state.get("user_query", "")
        .lower()
    )

    if "forecast" in user_query:

        return "forecast"

    if "anomaly" in user_query:

        return "anomaly"

    if "trend" in user_query:

        return "insight"

    return "default"