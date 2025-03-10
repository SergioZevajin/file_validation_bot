import logging

# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Обработчик для записи в файл
file_handler = logging.FileHandler("bot.log", mode="a")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

# Добавляем обработчики в логгер
logger.addHandler(file_handler)
logger.addHandler(console_handler)
