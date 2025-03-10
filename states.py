from aiogram.dispatcher.filters.state import State, StatesGroup

class PDFCheckState(StatesGroup):
    waiting_for_pdf = State()
