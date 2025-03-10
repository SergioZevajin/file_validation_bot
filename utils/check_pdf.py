from aiogram.types import Document

def is_pdf(document: Document) -> bool:

    return document.mime_type == "application/pdf"
