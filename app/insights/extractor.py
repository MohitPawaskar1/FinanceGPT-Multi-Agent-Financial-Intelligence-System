from app.insights.trends import (
    generate_revenue_insights
)

from app.insights.risk_signals import (
    detect_financial_risks
)

from app.insights.formatter import (
    format_insights
)


def generate_dataset_insights(df):

    insights = []

    revenue_insights = (
        generate_revenue_insights(df)
    )

    risks = detect_financial_risks(df)

    insights.extend(revenue_insights)

    insights.extend(risks)

    formatted_insights = format_insights(
        insights
    )

    return formatted_insights