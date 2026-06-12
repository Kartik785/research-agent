from research.utils.pdf_generator import generate_report_pdf
import importlib
from research.prompt_library.writer_agent import WRITER_PROMPT
from research.state.agent_state import AgentState
def writer(state: AgentState):

    print("writer agent called")

    llm_mod = importlib.import_module("research.llm.llm_groq")
    llms = getattr(llm_mod, "llms")

    data = state["messages"][-1].content

    report = llms.invoke(
        WRITER_PROMPT +
        "\n\nResearch Data:\n" +
        data
    )

    pdf_path = generate_report_pdf(
        report.content
    )

    return {
        "messages": [report],   # <-- important
        "report": report.content,
        "pdf_path": pdf_path
    }