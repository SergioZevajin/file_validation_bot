import json
import datetime
import re

def format_prf(metadata):

    if metadata:
        metadata_dict = metadata[0]
    else:
        metadata_dict = {}

    pdf_metadata = {
        "Имя файла": metadata_dict.get("File:FileName", "Неизвестно"),
        "Размер (байт)": metadata_dict.get("File:FileSize", 0),
        "Версия PDF": metadata_dict.get("PDF:PDFVersion", "Не указано"),
        "Количество страниц": metadata_dict.get("PDF:PageCount", "Неизвестно"),
        "Создатель": metadata_dict.get("PDF:Creator", "Неизвестно"),
        "Программа": metadata_dict.get("PDF:Producer", "Неизвестно"),
        "Дата создания": metadata_dict.get("PDF:CreateDate", "Нет данных"),
        "Дата изменения": metadata_dict.get("PDF:ModifyDate", "Нет изменений"),
        "Название": metadata_dict.get("PDF:Title", "Без названия"),
        "Автор": metadata_dict.get("PDF:Author", "Неизвестен"),
        "Внимание": metadata_dict.get("Warning", "-----"),
    }

    if pdf_metadata["Размер (байт)"] > 0:
        pdf_metadata["Размер (КБ)"] = round(pdf_metadata["Размер (байт)"] / 1024, 1)
        pdf_metadata.pop("Размер (байт)", None)


    if pdf_metadata["Дата создания"] != "Нет данных":
        date_str = pdf_metadata["Дата создания"]
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S%z")
        except ValueError:
            date_obj = datetime.datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")

        pdf_metadata["Дата создания"] = date_obj.strftime("%d %B %Y, %H:%M")

    if pdf_metadata["Дата изменения"] != "Нет изменений":
        pdf_metadata["Оргинальный ли файл"] = "❌ Нет"
    else:
        pdf_metadata["Оргинальный ли файл"] = "✅ Да"

    emoji_map = {
        "Имя файла": "📄",
        "Размер (КБ)": "📏",
        "Версия PDF": "📜",
        "Количество страниц": "📄",
        "Создатель": "🖊",
        "Программа": "🛠",
        "Дата создания": "📅",
        "Дата изменения": "🕒",
        "Название": "📑",
        "Автор": "👤",
        "Внимание": "⚠️",
        "Оргинальный ли файл":  "🔄",
    }


    lines = []


    for key, value in pdf_metadata.items():
        if value:
            emoji = emoji_map.get(key, "📄")
            lines.append(f"{emoji}   {key}:  {value}")

    result_text = "\n".join(lines)

    return result_text