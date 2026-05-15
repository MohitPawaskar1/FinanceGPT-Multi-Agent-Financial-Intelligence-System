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

from app.anomaly_detection.visualization import (
    plot_anomalies
)


def run_anomaly_pipeline():

    file_path = (
        "datasets/sample_financial_data.csv"
    )

    df = load_financial_data(file_path)

    df = preprocess_financial_data(df)

    df = standardize_schema(df)

    anomaly_df = detect_anomalies(df)

    print("\nANOMALY RESULTS:\n")

    print(anomaly_df)

    summary = generate_anomaly_summary(
        anomaly_df
    )

    print("\nANOMALY SUMMARY:\n")

    print(summary)

    plot_anomalies(
        anomaly_df,
        "revenue"
    )


if __name__ == "__main__":
    run_anomaly_pipeline()