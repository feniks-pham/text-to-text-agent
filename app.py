import streamlit as st
import google.generativeai as genai

st.title("Chatbot với Google Gemini API")

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash-lite")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Bạn:", key="user_input")

if st.button("Gửi") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Đang trả lời..."):
        response = model.generate_content(user_input)
        bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Bạn:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")