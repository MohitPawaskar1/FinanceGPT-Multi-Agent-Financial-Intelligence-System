def select_primary_metric(
    numeric_columns
):

    priority_keywords = [

        "sales",
        "revenue",
        "profit",
        "price",
        "income",
        "amount",
        "value",
        "cpi",
        "unemployment"
    ]

    for keyword in priority_keywords:

        for col in numeric_columns:

            if keyword in col.lower():

                return col

    if numeric_columns:

        return numeric_columns[0]

    return None