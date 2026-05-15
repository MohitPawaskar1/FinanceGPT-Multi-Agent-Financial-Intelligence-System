import matplotlib.pyplot as plt


def plot_anomalies(
    df,
    target_column
):

    normal = df[
        df["anomaly"] == 1
    ]

    anomalies = df[
        df["anomaly"] == -1
    ]

    plt.figure(figsize=(10, 5))

    plt.scatter(
        normal.index,
        normal[target_column],
        label="Normal"
    )

    plt.scatter(
        anomalies.index,
        anomalies[target_column],
        label="Anomaly"
    )

    plt.title(
        f"Anomaly Detection - {target_column}"
    )

    plt.xlabel("Index")

    plt.ylabel(target_column)

    plt.legend()

    plt.show()