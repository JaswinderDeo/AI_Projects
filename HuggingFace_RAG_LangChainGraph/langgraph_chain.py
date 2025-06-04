from typing import List
# ✅ Updated imports from new supported packages
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel

import os
from dotenv import load_dotenv
load_dotenv()

# Load your documents for RAG
doc_loader = TextLoader("./knowledge_base.txt")
documents = doc_loader.load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(documents)

# Create vector store index
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(split_docs, embedding)
retriever = vectorstore.as_retriever()

# Define LLM
gpt4 = ChatOpenAI(model_name="gpt-4")

# Define input schema
class QueryInput(BaseModel):
    query: str
    user_id: str

# Define agent state
class AgentState(BaseModel):
    query: str
    user_id: str
    retrieved_docs: List[str] = []
    answer: str = ""

# Define retrieval node
def retrieve_docs(state: AgentState) -> AgentState:
    docs = retriever.get_relevant_documents(state.query)
    state.retrieved_docs = [doc.page_content for doc in docs]
    return state

# Define answer generation node
def generate_answer(state: AgentState) -> AgentState:
    rag_chain = RetrievalQA.from_chain_type(llm=gpt4, retriever=retriever)
    state.answer = rag_chain.run(state.query)
    return state

# Create LangGraph graph
graph_builder = StateGraph(AgentState)
graph_builder.add_node("retrieval", RunnableLambda(retrieve_docs))
graph_builder.add_node("generation", RunnableLambda(generate_answer))
graph_builder.set_entry_point("retrieval")
graph_builder.add_edge("retrieval", "generation")

graph = graph_builder.compile()
print("\n🧭 LangGraph Structure:")
graph.get_graph().print_ascii()

if __name__ == "__main__":
    # Simulated user input
    user_query = "How does memory work in LangGraph?"
    user_id = "user_123"

    # Create agent state
    initial_state = AgentState(query=user_query, user_id=user_id)

    # Invoke the graph
    result = graph.invoke(initial_state)

    # Print final output
    print("\n✅ Final Answer:")
    print("Query:", result['query'])
    print("Answer:", result['answer'])
