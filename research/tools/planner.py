
import importlib
from research.state.agent_state import AgentState

def planner(state: AgentState):
     # lazy import to avoid circular import / attribute errors
     llm_mod = importlib.import_module("research.llm.llm_groq")
     llms = getattr(llm_mod, "llms")

     # extract a user-facing query from the incoming messages
     msgs = state.get("messages") or []
     user_msg = None
     if msgs:
          last = msgs[-1]
          user_msg = getattr(last, "content", str(last))

     prompt = f"""
          Decide whether this query requires
          real-time web search.

          Query: {user_msg or state.get('query', '')}

          Return only:
          SEARCH
          or
          NO_SEARCH
          """

     response = llms.invoke(prompt)
     # some LLM responses may store text in `content`; fallback to str(response)
     content = getattr(response, "content", None) or str(response)
     decision = content.strip().upper()

     # If decision is SEARCH, generate an AIMessage via llm_with_tools
     if decision == "SEARCH":
          llm_with_tools = getattr(llm_mod, "llm_with_tools", None)
          if llm_with_tools is None:
               return {"decision": decision, "messages": state.get("messages")}

          model_input = msgs if msgs else [user_msg]
          model_response = llm_with_tools.invoke(model_input)
          return {"decision": decision, "messages": [model_response]}

     return {"decision": decision, "messages": state.get("messages")}

def routes(state):
        if state['decision'] == "SEARCH":
            return "tools"
        else:
            return "llm"
# here i have defined the path_map for the conditional edge from planner node to tools and llm node based on the decision made by the planner node. If the decision is SEARCH then it will go to tools node otherwise it will go to llm node..