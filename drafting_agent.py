# agents/drafting_agent.py

# agents/drafting_agent.py

from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def drafting_agent(state):
    research_output = state["output"]  # ⭐ Expecting dict with "output" key
    prompt = [
        SystemMessage(content="You are a professional writer. Create a well-written answer from the given research."),
        HumanMessage(content=f"Research Summary:\n{research_output}")
    ]
    response = llm(prompt)
    return {"final_answer": response.content}  # ⭐ Must return a dict
