import json
import re

from app.core.llm import get_llm

from app.prompts.schema_mapping_prompt import (
    SCHEMA_MAPPING_PROMPT
)


def clean_json_response(response_text: str):

    response_text = response_text.strip()

    response_text = re.sub(
        r"^```json",
        "",
        response_text
    )

    response_text = re.sub(
        r"```$",
        "",
        response_text
    )

    response_text = response_text.strip()

    return response_text


def analyze_dataset_schema(df):

    llm = get_llm()

    columns = list(df.columns)

    sample_data = df.head(5).to_dict()

    prompt = SCHEMA_MAPPING_PROMPT.format(
        columns=columns,
        sample_data=sample_data
    )

    response = llm.invoke(prompt)

    content = response.content

    cleaned_content = clean_json_response(content)

    try:

        parsed_response = json.loads(
            cleaned_content
        )

        return parsed_response

    except Exception as e:

        print("\nERROR PARSING LLM RESPONSE\n")

        print(cleaned_content)

        raise e