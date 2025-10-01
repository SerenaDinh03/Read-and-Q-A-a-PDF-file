import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from src.agents.workflows.pdf_reader_workflow import build_pdf_agent

console = Console()

if __name__ == "__main__":
    # Set API key cho Gemini
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = "YOUR_API_HERE"

    pdf_path = r"D:\Checking\ReadPDF\VAI_AI Engineer – Robotics Perception.docx.pdf"

    try:
        agent = build_pdf_agent(pdf_path)
        console.print("[green]-->PDF Reader Agent đã được khởi tạo thành công![/green]")
    except Exception as e:
        console.print(f"[bold red]Lỗi khởi tạo agent: {e}[/bold red]")
        exit(1)

    console.print(Panel.fit("[bold cyan]PDF READER AGENT DEMO[/bold cyan]", style="cyan"))
    console.print("[yellow]-->Nhập câu hỏi về tài liệu PDF (gõ 'quit' để thoát')[/yellow]\n")

    while True:
        query = Prompt.ask("[bold green]👤 Bạn[/bold green]")
        if query.lower() in ["quit", "exit"]:
            console.print("[blue]Tạm biệt![/blue]")
            break

        try:
            answer = agent.run(query)
            console.print(Panel(answer, title="--> Agent", subtitle="Kết quả", style="magenta"))
        except Exception as e:
            console.print(f"[bold red]Lỗi: {e}[/bold red]")

