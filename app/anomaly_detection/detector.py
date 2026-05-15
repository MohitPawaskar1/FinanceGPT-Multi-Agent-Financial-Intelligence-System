from sklearn.ensemble import (
    IsolationForest
)

from app.anomaly_detection.preprocessing import (
    prepare_anomaly_features
)


def detect_anomalies(df):

    numeric_df = prepare_anomaly_features(
        df
    )

    model = IsolationForest(
    contamination="auto",
    random_state=42
)

    predictions = model.fit_predict(
        numeric_df
    )

    result_df = df.copy()

    result_df["anomaly"] = predictions

    return result_df