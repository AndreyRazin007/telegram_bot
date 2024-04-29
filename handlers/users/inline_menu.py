from loader import dispatcher

from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import inline_menu

@dispatcher.message_handler(text="Инлайн меню")
async def show_inline_menu(message: types.Message):
    await message.answer("Выберите тему", reply_markup=inline_menu)

@dispatcher.callback_query_handler(text="Сообщение")
async def send_message(call: CallbackQuery):
    await call.message.answer("Введите сообщение")
