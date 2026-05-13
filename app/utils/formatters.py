def format_numeric_value(value):

    if isinstance(value, (int, float)):

        return round(value, 2)

    return value