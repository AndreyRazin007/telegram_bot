from aiogram import types
from loader import dispatcher

@dispatcher.message_handler()
async def command_error(message: types.Message):
    await message.answer(f"Команда {message.text} не найдена!")
