import streamlit as st
import requests

st.set_page_config(page_title="DocQA Chatbot", layout="centered")
st.title("📄 Document Chatbot")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    res = requests.post("http://localhost:8000/upload/", files=files)
    st.success(f"Uploaded: {uploaded_file.name}")
    st.json(res.json())

query = st.text_input("Ask a question about the documents")

if query:
    st.write("🔍 Searching for answers... (Feature coming soon)")
