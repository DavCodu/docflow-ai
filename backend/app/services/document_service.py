import os
from pathlib import Path
from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Автоматично създава папка uploads, ако липсва


async def save_and_extract_text(file: UploadFile) -> dict:
    # 1. Запазваме файла на диска
    file_path = UPLOAD_DIR / file.filename
    content = await file.read()
    
    with open(file_path, "wb") as f:
        f.write(content)

    # 2. Извличаме текста според типа на файла
    extracted_text = ""
    file_ext = file.filename.split(".")[-1].lower() if "." in file.filename else ""

    if file_ext == "txt":
        extracted_text = content.decode("utf-8", errors="ignore")

    elif file_ext == "pdf":
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

    elif file_ext == "docx":
        doc = Document(file_path)
        extracted_text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

    return {
        "file_path": str(file_path),
        "text_length": len(extracted_text),
        "preview": extracted_text[:300] + "..." if len(extracted_text) > 300 else extracted_text,
        "full_text": extracted_text
    }