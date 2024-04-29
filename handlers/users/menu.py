from keyboards.default import keyboard_menu

from loader import dispatcher
from aiogram import types

@dispatcher.message_handler(commands=["menu"])
async def command_menu(message: types.Message):
    await message.answer("Выберите тему", reply_markup=keyboard_menu)
