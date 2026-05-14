from app.core.llm import get_llm

from app.agents.prompts import (
    COMMENTARY_PROMPT
)


def generate_financial_commentary(insights):

    llm = get_llm()

    prompt = COMMENTARY_PROMPT.format(
        insights=insights
    )

    response = llm.invoke(prompt)

    return response.content