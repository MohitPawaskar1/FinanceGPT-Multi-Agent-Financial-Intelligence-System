from app.orchestration.workflow import (
    build_workflow
)


def test_workflow():

    workflow = build_workflow()

    state = {

        "file_path":
        "datasets/sample_financial_data.csv",

        "user_query":
        "Will business growth continue next quarter?"
    }

    result = workflow.invoke(state)

    print("\nFINAL STATE:\n")

    for key, value in result.items():

        print(f"\n{key}:\n")

        print(value)


if __name__ == "__main__":
    test_workflow()