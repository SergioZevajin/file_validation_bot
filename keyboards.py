from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(KeyboardButton("Проверить PDF"))


cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_keyboard.add(KeyboardButton("Отмена"))


choose_function_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
choose_function_keyboard.add(KeyboardButton("Выбрать функцию"))

