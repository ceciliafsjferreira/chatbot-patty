import streamlit as st
from google import genai 

st.header('Olá! Sou a Patty!', divider=True)
st.write('Posso te ajudar a aprender sobre Linguagem de Programação Python.')

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

messages = st.session_state["messages"]

for m in messages:
    with st.chat_message(m['role']):
        st.write(m['content'])

user_message = st.chat_input("Escreva sua dúvida aqui...")

if user_message:
    messages.append({'role': 'user', 'content': user_message})
    with st.chat_message('user'):
        st.write(user_message)

    contents = [m["content"] for m in messages if m.get("content")]

    response = client.models.generate_content(model="gemini-3.5-flash", contents=contents)
    
    of_chat = response.text
    
    with st.chat_message("assistant"):st.write(of_chat)
        
    st.session_state["messages"].append({"role": "assistant", "content": of_chat})
 
   