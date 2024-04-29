from aiogram import types
from loader import dispatcher

@dispatcher.message_handler(text="Привет")
async def command_hello(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}!")