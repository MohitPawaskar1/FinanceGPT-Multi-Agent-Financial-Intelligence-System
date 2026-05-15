import streamlit as st
import requests


st.title("Financial Query Assistant")

query = st.text_input(
    "Ask a financial question"
)

if st.button("Submit Query"):

    with st.spinner(
        "Generating response..."
    ):

        response = requests.post(
            "http://127.0.0.1:8000/query/run",
            json={
                "query": query
            }
        )

        result = response.json()

    st.subheader("AI Response")

    st.write(result["response"])