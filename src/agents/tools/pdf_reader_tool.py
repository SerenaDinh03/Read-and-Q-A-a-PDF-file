from typing import ClassVar
from langchain.tools import BaseTool
from src.utils.file_utils import extract_text_from_pdf
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class PDFReaderTool(BaseTool):
    name: ClassVar[str] = "PDFQuestionAnswering"
    description: ClassVar[str] = "Trả lời câu hỏi từ nội dung file PDF bằng Gemini"

    pdf_path: str
    pdf_text: str = ""
    model: ChatGoogleGenerativeAI = None

    def __init__(self, pdf_path: str, **kwargs):
        super().__init__(pdf_path=pdf_path, **kwargs)  
        self.pdf_text = extract_text_from_pdf(pdf_path)
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.environ["GOOGLE_API_KEY"],
            temperature=0.0,
        )

    def _run(self, query: str) -> str:
        from langchain.schema import HumanMessage
        messages = [
            HumanMessage(
                content=f"Nội dung PDF:\n{self.pdf_text}\n\nCâu hỏi: {query}"
            )
        ]
        resp = self.model(messages)
        return resp.content if hasattr(resp, "content") else str(resp)

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("PDFReaderTool chưa hỗ trợ async")
