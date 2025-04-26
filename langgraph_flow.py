# langgraph_flow.py
# langgraph_flow.py

from langgraph.graph import StateGraph, END
from my_agents.research_agent import research_agent
from my_agents.drafting_agent import drafting_agent
from typing import TypedDict

# Step 1: Define the State
class AgentState(TypedDict):
    input: str            # Scraped website content
    output: str           # Research agent's summarized output
    final_answer: str     # Drafting agent's written answer

# Step 2: Build the graph
def build_graph():
    # Pass the state model here
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("research", research_agent)
    workflow.add_node("draft", drafting_agent)

    # Set entry point and connections
    workflow.set_entry_point("research")
    workflow.add_edge("research", "draft")
    workflow.add_edge("draft", END)

    # Return compiled graph
    return workflow.compile()

