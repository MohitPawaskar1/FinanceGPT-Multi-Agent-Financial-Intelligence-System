def detect_date_columns(df):

    possible_dates = []

    for col in df.columns:

        col_lower = col.lower()

        if (
            "date" in col_lower
            or "time" in col_lower
            or "year" in col_lower
        ):

            possible_dates.append(col)

    return possible_dates


def detect_numeric_targets(df):

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    ignored_keywords = [
        "store",
        "id",
        "index"
    ]

    filtered = []

    for col in numeric_cols:

        col_lower = col.lower()

        if not any(
            keyword in col_lower
            for keyword in ignored_keywords
        ):

            filtered.append(col)

    return filtered