from dotenv import load_dotenv
import os
from research.state.agent_state import AgentState
from research.tools.tools import tools
from research.tools.planner import planner, routes
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from research.prompt_library.search import search_prompt
from research.tools.writer import writer

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")    

from langchain_groq import ChatGroq

llms = ChatGroq(model = "llama-3.3-70b-versatile", groq_api_key=groq_api_key)

from langchain_core.messages import HumanMessage , SystemMessage , AIMessage

llm_with_tools = llms.bind_tools(tools)


def research(state: AgentState):
    user_message =state["messages"]
    input = [SystemMessage(content=search_prompt)] + user_message
    research_result = llm_with_tools.invoke(input)
    print(research_result.tool_calls)
    return{
        "messages":[research_result]
    }

fun2 = ToolNode(tools)


workflow = StateGraph(AgentState)
workflow.add_node("research", research)
workflow.add_node("planner", planner)
workflow.add_node("writer", writer)
workflow.add_node("tools", fun2)

workflow.add_edge(START, "planner")
# workflow.add_conditional_edges("llm", tools_condition)
# workflow.add_edge("tools", "llm")
workflow.add_conditional_edges("planner" , routes )
workflow.add_edge("tools", "research")
workflow.add_edge("research", "writer")
workflow.add_edge("writer", END)

app = workflow.compile()


