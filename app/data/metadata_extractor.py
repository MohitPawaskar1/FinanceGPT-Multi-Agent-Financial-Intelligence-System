import pandas as pd


def extract_metadata(df: pd.DataFrame):

    metadata = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_columns": list(
            df.select_dtypes(include=["number"]).columns
        ),
        "categorical_columns": list(
            df.select_dtypes(include=["object"]).columns
        )
    }

    return metadata