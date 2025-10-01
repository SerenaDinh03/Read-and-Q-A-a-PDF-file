from langchain.agents import initialize_agent, AgentType
from src.agents.tools.pdf_reader_tool import PDFReaderTool
from langchain_google_genai import ChatGoogleGenerativeAI  
import os

def build_pdf_agent(pdf_path = str):
    model = ChatGoogleGenerativeAI(
        model = "gemini-2.0-flash",
        google_api_key = os.environ["GOOGLE_API_KEY"],
        temperature = 0.0,
    )

    tools = [PDFReaderTool(pdf_path=pdf_path)]
    agent = initialize_agent(tools, model, agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)

    return agent