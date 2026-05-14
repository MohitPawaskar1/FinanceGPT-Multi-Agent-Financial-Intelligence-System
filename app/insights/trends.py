import pandas as pd


def generate_revenue_insights(df: pd.DataFrame):

    insights = []

    if "revenue" not in df.columns:
        return insights

    growth = (
        df["revenue"]
        .pct_change()
        .dropna()
        * 100
    )

    if len(growth) == 0:
        return insights

    average_growth = growth.mean()

    max_growth = growth.max()

    insights.append(
        f"Average revenue growth was {average_growth:.2f}%."
    )

    insights.append(
        f"Maximum revenue growth reached {max_growth:.2f}%."
    )

    if average_growth > 0:
        insights.append(
            "Revenue showed an overall upward trend."
        )

    return insights