import streamlit as st
from main_query import main_query

st.set_page_config(page_title="COS Chatbot", layout="wide")
st.title("📄 IITD Courses of Study Chatbot")
st.markdown("Ask a question based on the Courses Of Study of IITD.")

query = st.text_input("🔍 Your Question")

if query:
    with st.spinner("Thinking..."):
        answer = main_query(query)

    st.success("✅ Answer:")
    st.markdown(answer)

