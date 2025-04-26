# agents/research_agent.py

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def research_agent(state):
    scraped_text = state["input"]  # ⭐ Expecting dict with "input" key
    prompt = [
        SystemMessage(content="You are a professional researcher. Extract important points from the following content."),
        HumanMessage(content=f"Here is the data:\n\n{scraped_text[:4000]}")
    ]
    response = llm(prompt)
    return {"output": response.content}  # ⭐ Must return a dict

