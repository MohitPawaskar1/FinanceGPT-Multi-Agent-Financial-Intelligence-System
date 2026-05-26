from fastapi import APIRouter

from pydantic import BaseModel

from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.forecasting.forecaster import (
    forecast_future_values
)

from app.forecasting.commentary import (
    generate_forecast_summary
)

from app.intelligence.column_detector import (

    detect_numeric_targets,

    detect_date_columns
)

from app.intelligence.target_selector import (
    select_forecast_target
)


router = APIRouter()


class ForecastRequest(BaseModel):

    file_path: str


@router.post("/forecast/run")

def run_forecast(
    request: ForecastRequest
):

    try:

        # =================================
        # LOAD DATA
        # =================================

        df = load_financial_data(
            request.file_path
        )

        df = preprocess_financial_data(
            df
        )

        # =================================
        # DETECT NUMERIC TARGETS
        # =================================

        numeric_columns = (
            detect_numeric_targets(df)
        )

        if len(numeric_columns) == 0:

            return {

                "summary":
                "No numeric targets available for forecasting."
            }

        # =================================
        # TARGET INFO
        # =================================

        target_info = (
            select_forecast_target(

                df,

                numeric_columns
            )
        )

        # =================================
        # EXTRACT TARGET COLUMN
        # =================================

        target_column = (
            target_info[
                "selected_target"
            ]
        )

        if target_column is None:

            return {

                "summary":
                "No valid forecast target detected."
            }

        # =================================
        # DATE DETECTION
        # =================================

        date_columns = (
            detect_date_columns(df)
        )

        if len(date_columns) == 0:

            return {

                "summary":
                "No valid date column detected."
            }

        date_column = (
            date_columns[0]
        )

        # =================================
        # FORECAST
        # =================================

        forecast_df = (
            forecast_future_values(

                df,

                target_column,

                date_column
            )
        )

        # =================================
        # SUMMARY
        # =================================

        summary = (
            generate_forecast_summary(
                forecast_df
            )
        )

        return {

            "summary": str(summary)
        }

    except Exception as e:

        return {

            "summary":
            f"Forecasting failed: {str(e)}"
        }