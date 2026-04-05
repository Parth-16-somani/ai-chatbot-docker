import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot (ML Domain)")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_input:
        try:
            response = requests.get(
                "http://backend:8000/chat",   # Docker URL
                params={"q": user_input}
            )

            if response.status_code == 200:
                st.success(response.json()["response"])
            else:
                st.error("Error from backend")

        except Exception as e:
            st.error("Backend not reachable")
            st.text(str(e))

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
.stTextInput input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("About")
st.sidebar.info("Domain: Machine Learning Chatbot")

st.markdown("### 💬 Ask anything about ML concepts")