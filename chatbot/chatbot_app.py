import streamlit as st
from chatbot.chatbot_v1_2 import workflow, ChatState
from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import HumanMessage

if 'messages' not in st.session_state:
  st.session_state['messages'] = []
  
CONFIG: RunnableConfig = {"configurable": {"thread_id": "1"}}

for messages in st.session_state.messages:
  with st.chat_message(messages["role"]):
    st.text(messages["content"]) 

user_input = st.chat_input("Ask me anything")

if user_input:
  
  st.session_state.messages.append({"role": "user", "content": user_input})
  
  init_state: ChatState = {'messages': [HumanMessage(user_input)]}
  
  final_state = workflow.invoke(init_state, config=CONFIG)
  
  with st.chat_message("user"):
    st.text(user_input)
  
  with st.chat_message("assistant"):
    st.text(final_state['messages'][-1].content)
  
  st.session_state.messages.append({"role": "assistant", "content": "Hello! How can I help you?"})