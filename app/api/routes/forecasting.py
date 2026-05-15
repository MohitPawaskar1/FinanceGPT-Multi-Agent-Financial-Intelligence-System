from fastapi import (
    APIRouter
)

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


router = APIRouter(
    prefix="/forecast",
    tags=["Forecasting"]
)


@router.post("/run")
def run_forecast():

    file_path = (
        "datasets/sample_financial_data.csv"
    )

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    forecast_df = forecast_future_values(
        df,
        target_column="revenue"
    )

    summary = generate_forecast_summary(
        forecast_df
    )

    return {
        "forecast":
        forecast_df.to_dict(),

        "summary":
        summary
    }