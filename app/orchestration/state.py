from typing import TypedDict

import pandas as pd


class FinanceState(TypedDict, total=False):

    file_path: str

    user_query: str

    route: str

    df: pd.DataFrame

    insights: str

    commentary: str

    anomaly_summary: str

    forecast_summary: str

    rag_response: str