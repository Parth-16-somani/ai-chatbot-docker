import streamlit as st
import requests

# Backend API URL
API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot")
st.write("Ask anything...")

# Input box
user_input = st.text_input("Your question:")

# Button
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a question")
    else:
        try:
            response = requests.post(
                API_URL,
                json={"message": user_input}
            )

            if response.status_code == 200:
                data = response.json()
                st.success(
    data.get("response") or 
    data.get("answer") or 
    data.get("message") or 
    "No response"
)
            else:
                st.error("Error from backend")

        except Exception as e:
            st.error(f"Connection error: {e}")

st.write(data)