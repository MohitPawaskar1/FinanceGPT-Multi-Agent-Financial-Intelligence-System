def generate_anomaly_summary(df):

    anomaly_count = (
        df["anomaly"] == -1
    ).sum()

    if anomaly_count == 0:

        return (
            "No significant anomalies "
            "were detected."
        )

    summary = f"""
Detected {anomaly_count}
potential anomalous records.

These records may indicate:
- unusual financial behavior
- unexpected operational changes
- abnormal transaction patterns
"""

    return summary