def format_insights(insights):

    formatted = "\n".join(
        [f"- {insight}" for insight in insights]
    )

    return formatted