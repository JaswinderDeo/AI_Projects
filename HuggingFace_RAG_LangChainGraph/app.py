import streamlit as st
from langgraph_chain import graph, AgentState

st.set_page_config(page_title="LangGraph RAG", layout="centered")

st.title("📚 LangGraph RAG Agent")
query = st.text_input("Ask a question:", placeholder="e.g., What is agent memory?")
user_id = "user_001"

if st.button("Submit Query") and query:
    with st.spinner("Thinking..."):
        state = AgentState(query=query, user_id=user_id)
        result = graph.invoke(state)
        st.success("Answer generated!")
        st.markdown("### 🔍 Answer:")
        st.write(result["answer"])