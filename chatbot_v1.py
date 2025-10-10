from langgraph.graph import StateGraph, START, END
from typing import List, TypedDict, Annotated
import operator
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(model='google_genai:gemini-2.5-flash')

class ChatState(TypedDict):
  messages: Annotated[List[BaseMessage], operator.add]
  
  
def chat(state: ChatState):

  response = llm.invoke(state['messages'])
  
  return {'messages': [response.content]}


graph = StateGraph(ChatState)

graph.add_node('chat', chat)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

workflow = graph.compile()


while True:
  user_query = input("you: ")
  
  if user_query == 'exit':
    print("good byee!")
    break
  
  init_state = {'messages': [HumanMessage(user_query)]}
  
  final_state = workflow.invoke(init_state)
  
  print(final_state['messages'][1])
  
  