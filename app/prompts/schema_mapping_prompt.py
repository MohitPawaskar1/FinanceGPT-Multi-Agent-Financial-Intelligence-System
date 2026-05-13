SCHEMA_MAPPING_PROMPT = """
You are a financial data schema analysis expert.

Your task is to analyze a dataset schema and identify semantic meanings of columns.

Dataset Columns:
{columns}

Sample Data:
{sample_data}

Identify:

1. Revenue-related columns
2. Expense-related columns
3. Profit-related columns
4. Date/time columns
5. Identifier columns
6. Irrelevant columns
7. Forecast target candidates

Return ONLY valid JSON.

Example Output:

{{
    "revenue_columns": [],
    "expense_columns": [],
    "profit_columns": [],
    "date_columns": [],
    "identifier_columns": [],
    "irrelevant_columns": [],
    "forecast_target_columns": []
}}
"""