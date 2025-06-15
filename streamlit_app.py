import streamlit as st
from main_query import main_query

api_key = st.secrets["OPENAI_API_KEY"]
st.set_page_config(page_title="COS Chatbot", layout="wide")
st.title("📄 IITD Courses of Study Chatbot")
st.markdown("Ask a question based on the Courses Of Study of IITD.")

query = st.text_input("🔍 Your Question")

if query:
    with st.spinner("Thinking..."):
        answer = main_query(query, api_key)

    st.success("✅ Answer:")
    st.markdown(answer)

