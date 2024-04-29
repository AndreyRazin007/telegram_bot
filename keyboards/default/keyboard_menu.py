from aiogram import types

keyboard_menu = types.ReplyKeyboardMarkup(
    keyboard = [
        [
            types.KeyboardButton(text="Первая тема"),
            types.KeyboardButton(text="Вторая тема"),
            types.KeyboardButton(text="Третья тема"),
        ]
    ],
    resize_keyboard=True
)
