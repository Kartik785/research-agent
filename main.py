from research.tools.tools import tools
from research.prompt_library.search import search_prompt
from langchain_core.messages import HumanMessage, SystemMessage
from research.llm.llm_groq import llm_with_tools
from research.llm.llm_groq import app
from research.state.agent_state import AgentState
from research.tools.planner import planner, routes
from research.tools.writer import writer
import streamlit as st

from langchain_core.messages import HumanMessage

from research.llm.llm_groq import app


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Research Assistant")

query = st.text_area(
    "Enter your research query:",
    height=150
)

if st.button("Generate Report"):

    if not query.strip():

        st.warning(
            "Please enter a query."
        )

    else:

        with st.spinner(
            "Researching and generating report..."
        ):

            result = app.invoke(
                {
                    "messages": [
                        HumanMessage(
                            content=query
                        )
                    ]
                }
            )

            st.success(
                "Report Generated Successfully"
            )

            st.subheader(
                "Generated Report"
            )

            st.markdown(
                result["report"]
            )

            with open(
                result["pdf_path"],
                "rb"
            ) as pdf_file:

                st.download_button(
                    label= " Download PDF",
                    data=pdf_file,
                    file_name="research_report.pdf",
                    mime="application/pdf"
                )