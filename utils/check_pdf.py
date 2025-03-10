from aiogram.types import Document

def is_pdf(document: Document) -> bool:
    """Проверяет, является ли загруженный файл PDF."""
    return document.mime_type == "application/pdf"
