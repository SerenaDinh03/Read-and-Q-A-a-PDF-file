from fastapi import APIRouter, UploadFile, Form
from src.agents.workflows.pdf_reader_workflow import build_pdf_agent
import tempfile

router = APIRouter(prefix="/pdf_reader", tags=["PDF Reader"])

@router.post("/ask")
async def ask_pdf_question(file: UploadFile, question: str = Form(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(await file.read())
        temp_pdf_path = temp_pdf.name

    agent = build_pdf_agent(pdf_path=temp_pdf_path)
    response = agent.run(question)

    return {"answer": response}