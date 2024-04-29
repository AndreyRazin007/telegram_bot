from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text="Сообщение", callback_data="Сообщение"),
                                           InlineKeyboardButton(text="Репозиторий",
                                                                url="https://github.com/AndreyRazin007/telegram_bot/tree/main")
                                       ]
                                    ])
