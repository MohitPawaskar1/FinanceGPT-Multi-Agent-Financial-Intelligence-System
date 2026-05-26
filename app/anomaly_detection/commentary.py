def generate_anomaly_summary(

    anomaly_count,

    target_column,

    max_value,

    avg_value
):

    if anomaly_count == 0:

        return f"""

No significant anomalies were detected.

The operational patterns within
{target_column} appear stable
and consistent with expected
business behavior.
"""

    return f"""

Detected {anomaly_count} statistically
significant anomalous records.

The analysis identified unusual
behavior within the {target_column}
metric, where certain transactions
deviated substantially from normal
operational patterns.

Observed anomalies include
high-value transactional activity
exceeding the average operational
range of {round(avg_value, 2)}.

The highest detected anomalous
value reached approximately
{round(max_value, 2)},
indicating potential premium
customer activity, exceptional
transactions, or irregular
business events requiring review.
"""