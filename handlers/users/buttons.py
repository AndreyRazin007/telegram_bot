from aiogram import types
from loader import dispatcher

@dispatcher.message_handler(text="Первая тема")
async def first_theme_button(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Ты выбрал {message.text}")

@dispatcher.message_handler(text="Вторая тема")
async def first_theme_button(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Ты выбрал {message.text}")


@dispatcher.message_handler(text="Третья тема")
async def first_theme_button(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Ты выбрал {message.text}")

