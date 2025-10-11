import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from chatbot.chatbot_app_backend import workflow, ChatState  
from langchain_core.runnables.config import RunnableConfig
from langchain_core.messages import HumanMessage

# Initialize session state for messages if not present
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

CONFIG: RunnableConfig = {"configurable": {"thread_id": "1"}}

# Display chat history
for message in st.session_state['messages']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

# User input
user_input = st.chat_input("Ask me anything")

if user_input:
    # Append user message to session state and display it
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Prepare initial state for workflow
    init_state: ChatState = {'messages': [HumanMessage(content=user_input)]}


    # Display and append assistant response
    with st.chat_message("assistant"):
        assistant_response = st.write_stream(
          message_chunk.content for message_chunk, metadata in workflow.stream(
            init_state, 
            config=CONFIG,
            stream_mode='messages',
            )
          )
    st.session_state['messages'].append({"role": "assistant", "content": assistant_response})