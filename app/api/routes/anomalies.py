from fastapi import APIRouter

from pydantic import BaseModel

from app.data.loader import (
    load_financial_data
)

from app.data.preprocessing import (
    preprocess_financial_data
)

from app.anomaly_detection.detector import (
    detect_anomalies
)

from app.anomaly_detection.commentary import (
    generate_anomaly_summary
)

from app.intelligence.column_detector import (
    detect_numeric_targets
)

from app.intelligence.target_selector import (
    select_forecast_target
)


router = APIRouter()


class AnomalyRequest(BaseModel):

    file_path: str


@router.post("/anomalies/run")

def run_anomaly_detection(
    request: AnomalyRequest
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
                "No numeric columns available for anomaly detection."
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

        target_column = (
            target_info[
                "selected_target"
            ]
        )

        # =================================
        # DETECT ANOMALIES
        # =================================

        anomaly_df = (
            detect_anomalies(

                df,

                target_column
            )
        )

        anomaly_count = len(
            anomaly_df
        )

        max_value = (
            anomaly_df[
                target_column
            ].max()
            if anomaly_count > 0
            else 0
        )

        avg_value = round(

            df[
                target_column
            ].mean(),

            2
        )

        # =================================
        # GENERATE SUMMARY
        # =================================

        summary = (
            generate_anomaly_summary(

                anomaly_count,

                target_column,

                max_value,

                avg_value
            )
        )

        return {

            "summary": summary
        }

    except Exception as e:

        return {

            "summary":
            f"Anomaly detection failed: {str(e)}"
        }