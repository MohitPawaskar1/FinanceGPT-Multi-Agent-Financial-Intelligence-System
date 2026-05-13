from app.core.llm import get_llm

def test_llm():
    llm = get_llm()

    response = llm.invoke("Explain what financial forecasting means in simple terms.")


    print("\nAI RESPONSE:\n")
    print(response.content)

if __name__ == "__main__":
    test_llm()