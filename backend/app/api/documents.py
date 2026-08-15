from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import save_and_extract_text

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    allowed_extensions = ["pdf", "txt", "docx"]
    file_ext = file.filename.split(".")[-1].lower() if "." in file.filename else ""
    
    if file_ext not in allowed_extensions:
        raise HTTPException(
            status_code=400, 
            detail=f"Неподдържан формат! Позволени са само: {', '.join(allowed_extensions)}"
        )

    # Записваме файла и извличаме текста
    result = await save_and_extract_text(file)

    return {
        "filename": file.filename,
        "message": "Файлът е качен и прочетен успешно! 📄",
        "file_path": result["file_path"],
        "text_length": result["text_length"],
        "text_preview": result["preview"]
    }