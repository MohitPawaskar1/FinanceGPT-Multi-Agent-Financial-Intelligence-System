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

from app.anomaly_detection.detector import (
    detect_anomalies
)

from app.anomaly_detection.commentary import (
    generate_anomaly_summary
)


router = APIRouter(
    prefix="/anomalies",
    tags=["Anomalies"]
)


@router.post("/run")
def run_anomaly_detection():

    file_path = (
        "datasets/sample_financial_data.csv"
    )

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    anomaly_df = detect_anomalies(df)

    summary = generate_anomaly_summary(
        anomaly_df
    )

    return {
        "results":
        anomaly_df.to_dict(),

        "summary":
        summary
    }