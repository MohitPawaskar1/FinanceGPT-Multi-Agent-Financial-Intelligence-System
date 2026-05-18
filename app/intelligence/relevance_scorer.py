import pandas as pd


def calculate_column_scores(
    df: pd.DataFrame,
    numeric_columns
):

    scores = {}

    priority_keywords = {

        "sales": 10,
        "revenue": 10,
        "profit": 10,
        "income": 9,
        "price": 7,
        "cost": 7,
        "amount": 8,
        "value": 7,
        "cpi": 6,
        "unemployment": 5,
        "temperature": 2
    }

    for col in numeric_columns:

        score = 0

        col_lower = col.lower()

        # Semantic keyword scoring

        for keyword, weight in (
            priority_keywords.items()
        ):

            if keyword in col_lower:

                score += weight

        # Variability scoring

        variance = df[col].var()

        if variance > 0:

            score += 3

        # Uniqueness scoring

        unique_ratio = (
            df[col].nunique() / len(df)
        )

        score += unique_ratio * 5

        scores[col] = round(score, 2)

    return scores


def get_top_targets(
    scores,
    top_k=3
):

    sorted_targets = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_targets[:top_k]


def calculate_confidence(
    top_targets
):

    if len(top_targets) < 2:

        return "High"

    top_score = top_targets[0][1]

    second_score = top_targets[1][1]

    difference = (
        top_score - second_score
    )

    if difference >= 5:

        return "High"

    elif difference >= 2:

        return "Medium"

    return "Low"