import pandas as pd

from app.data.validator import validate_file_path


def load_financial_data(file_path: str) -> pd.DataFrame:

    validate_file_path(file_path)

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")

    return df