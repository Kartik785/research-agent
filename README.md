# AI Research Agent

An AI-powered research assistant that automates topic research, information gathering, analysis, and report generation. The system uses a multi-agent workflow to plan research tasks, collect information, and generate structured reports with PDF export support.

## Features

- Automated topic research
- Multi-agent workflow architecture
- Structured report generation
- PDF export functionality
- Interactive user interface
- Modular and extensible design

## Tech Stack

- Python
- Streamlit
- LangGraph
- Pydantic
- ReportLab
- FastAPI
- Git/GitHub

## Architecture

User Query
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Report Generator
    ↓
PDF Export

## Run

pip install -r requirements.txt

streamlit run main.py
