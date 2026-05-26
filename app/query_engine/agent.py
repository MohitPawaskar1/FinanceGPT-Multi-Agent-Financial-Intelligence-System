from app.core.llm import (
    get_llm
)


# =========================================
# QUERY ENGINE
# =========================================

def answer_financial_query(

    query,

    df
):

    # =====================================
    # DATASET CONTEXT
    # =====================================

    dataset_columns = (
        ", ".join(df.columns)
    )

    dataset_shape = (
        f"{df.shape[0]} rows and {df.shape[1]} columns"
    )

    # =====================================
    # PROMPT
    # =====================================

    prompt = f"""

You are an executive financial AI assistant.

Answer the user's business question
using the uploaded financial dataset.

Dataset Information:
- Shape: {dataset_shape}
- Columns: {dataset_columns}

User Query:
{query}

Provide:
- concise business insights
- executive-level interpretation
- operational observations
- financial trends if relevant

Keep response professional and clear.
"""

    # =====================================
    # LLM
    # =====================================

    llm = get_llm()

    response = llm.invoke(
        prompt
    )

    return response.content