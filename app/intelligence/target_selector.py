from app.intelligence.relevance_scorer import (
    calculate_column_scores,
    get_top_targets,
    calculate_confidence
)


def select_forecast_target(
    df,
    numeric_columns
):

    if not numeric_columns:

        return None

    scores = calculate_column_scores(
        df,
        numeric_columns
    )

    top_targets = get_top_targets(scores)

    confidence = calculate_confidence(
        top_targets
    )

    best_column = top_targets[0][0]

    return {

        "selected_target":
        best_column,

        "confidence":
        confidence,

        "top_targets":
        top_targets,

        "scores":
        scores
    }