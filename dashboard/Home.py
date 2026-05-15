import streamlit as st


st.set_page_config(
    page_title="FinanceGPT",
    layout="wide"
)


st.title("FinanceGPT")

st.markdown("""
AI-Powered Multi-Agent Financial Intelligence Platform
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="Forecasting",
        value="Enabled"
    )

with col2:

    st.metric(
        label="RAG Memory",
        value="Active"
    )

with col3:

    st.metric(
        label="Agentic Routing",
        value="Running"
    )

st.divider()

st.subheader("Platform Capabilities")

st.markdown("""
- Financial Data Analysis
- Forecasting Intelligence
- Anomaly Detection
- AI Commentary Generation
- ChromaDB Semantic Memory
- LangGraph Multi-Agent Orchestration
""")

st.divider()

st.info(
    "Use the sidebar to navigate through FinanceGPT modules."
)