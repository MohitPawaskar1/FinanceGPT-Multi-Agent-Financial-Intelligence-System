def generate_forecast_summary(
    forecast_df
):

    average_forecast = (
        forecast_df["forecast"]
        .mean()
    )

    max_forecast = (
        forecast_df["forecast"]
        .max()
    )

    summary = f"""
Forecast Summary

Average Forecasted Value:
{average_forecast:.2f}

Maximum Forecasted Value:
{max_forecast:.2f}

The forecasting model predicts
continued growth trends based on
historical financial performance.
"""

    return summary