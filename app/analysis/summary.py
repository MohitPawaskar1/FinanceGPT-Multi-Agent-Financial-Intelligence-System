from app.analysis.metrics import generate_basic_kpis


def generate_financial_summary(df):

    metrics = generate_basic_kpis(df)

    summary = "Financial Performance Summary\n\n"

    for key, value in metrics.items():

        formatted_key = (
            key.replace("_", " ")
            .title()
        )

        summary += f"{formatted_key}: {value}\n"

    return summary