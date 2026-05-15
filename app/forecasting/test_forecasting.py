from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.data.schema_mapper import (
    standardize_schema
)

from app.forecasting.forecaster import (
    forecast_future_values
)

from app.forecasting.commentary import (
    generate_forecast_summary
)

from app.forecasting.visualization import (
    plot_forecast
)


def run_forecasting_pipeline():

    file_path = (
        "datasets/sample_financial_data.csv"
    )

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    forecast_df = forecast_future_values(
        df,
        target_column="revenue",
        periods=3
    )

    print("\nFORECAST RESULTS:\n")

    print(forecast_df)

    summary = generate_forecast_summary(
        forecast_df
    )

    print("\nFORECAST SUMMARY:\n")

    print(summary)

    plot_forecast(
        df,
        forecast_df,
        "revenue"
    )


if __name__ == "__main__":
    run_forecasting_pipeline()