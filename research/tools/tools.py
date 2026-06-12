# wikipedia , tavily_search , financ 
import os

from dotenv import load_dotenv
from langchain_community.tools import WikipediaQueryRun, tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.tools import Tool

from research import llm
from research.prompt_library.search import RESEARCH_PROMPT

load_dotenv()

api_wrapper = WikipediaAPIWrapper(top_k=5, return_source_documents=True)
weki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

tools = [weki_tool]

tavily_api_key = os.getenv("TAVILY_API_KEY")
if tavily_api_key:
    from langchain_community.tools.tavily_search import TavilySearchResults

    tavily_tool = TavilySearchResults(tavily_api_key=tavily_api_key)
    tools.append(tavily_tool)



