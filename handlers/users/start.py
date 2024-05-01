from aiogram import types
from loader import dispatcher

@dispatcher.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Чтобы получить свой стикерпак, "
                         "загрузи свою фотографию и выбери тему стикерпака!")
