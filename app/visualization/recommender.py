def recommend_chart_type(

    df,

    date_columns,

    numeric_columns,

    target_column
):

    # =====================================
    # TRUE TIME SERIES
    # =====================================

    if len(date_columns) > 0:

        return "line"

    # =====================================
    # MULTI NUMERIC
    # =====================================

    if len(numeric_columns) >= 2:

        return "scatter"

    # =====================================
    # SINGLE NUMERIC
    # =====================================

    if len(numeric_columns) == 1:

        return "histogram"

    # =====================================
    # FALLBACK
    # =====================================

    return "bar"