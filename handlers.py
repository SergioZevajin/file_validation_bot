import json
import os
import tempfile
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from utils.check_pdf import is_pdf
from utils.extract_metadata import get_pdf_metadata
from keyboards import start_keyboard, cancel_keyboard, choose_function_keyboard
from states import PDFCheckState
from logger import logger
from utils.format_metadata import format_prf


async def start_cmd(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} {message.from_user.full_name} вызвал /start")
    await message.reply("Выберите функцию:", reply_markup=start_keyboard)

async def ask_for_pdf(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} нажал 'Проверить PDF'")
    await PDFCheckState.waiting_for_pdf.set()
    await message.reply("Отправьте мне PDF-файл для проверки.", reply_markup=cancel_keyboard)

async def handle_document(message: types.Message, state: FSMContext):
    if not is_pdf(message.document):
        await message.reply("Это не PDF-файл! Попробуйте снова или нажмите 'Отмена'.")
        return

    try:
        file = await message.bot.download_file_by_id(message.document.file_id)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name

        metadata = get_pdf_metadata(temp_file_path)
        metadata = json.loads(metadata)
        os.unlink(temp_file_path)


        formatted_text = format_prf(metadata)


        await state.finish()
        await message.reply(formatted_text, reply_markup=choose_function_keyboard)
    except Exception as e:
        logger.error(f"Ошибка обработки PDF: {e}")
        await message.reply("Произошла ошибка при обработке файла. Попробуйте снова.")
        await state.finish()

async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("Операция отменена. Выберите функцию:", reply_markup=start_keyboard)

async def choose_function(message: types.Message):
    await message.reply("Выберите нужную функцию из доступных:", reply_markup=start_keyboard)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
    dp.register_message_handler(ask_for_pdf, lambda message: message.text == "Проверить PDF")
    dp.register_message_handler(handle_document, state=PDFCheckState.waiting_for_pdf, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(cancel_action, lambda message: message.text == "Отмена", state=PDFCheckState.waiting_for_pdf)
    dp.register_message_handler(choose_function, lambda message: message.text == "Выбрать функцию")
