from sklearn.ensemble import (
    IsolationForest
)


# =========================================
# ANOMALY DETECTION ENGINE
# =========================================

def detect_anomalies(

    df,

    target_column
):

    # =====================================
    # PREPARE DATA
    # =====================================

    anomaly_df = df[[
        target_column
    ]].copy()

    # =====================================
    # BUILD MODEL
    # =====================================

    model = IsolationForest(

        contamination=0.02,

        random_state=42
    )

    # =====================================
    # DETECT OUTLIERS
    # =====================================

    anomaly_df["anomaly"] = (
        model.fit_predict(
            anomaly_df
        )
    )

    # =====================================
    # FILTER ANOMALIES
    # =====================================

    anomalies = df[
        anomaly_df["anomaly"] == -1
    ]

    return anomalies