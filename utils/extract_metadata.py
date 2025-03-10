import exiftool

def get_pdf_metadata(file_path):
    with exiftool.ExifTool() as et:
        metadata = et.execute("-j", file_path)  # ExifTool уже возвращает строку

    return metadata
