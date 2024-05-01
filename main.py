from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

import os

from aiogram import executor, Dispatcher, types
from aiogram.types import ContentType, Message

from handlers import dispatcher

from user_data import UserData

import json
from datetime import datetime

@dispatcher.message_handler(content_types=ContentType.PHOTO)
async def photo_handler_user(message: Message):
    username = message.from_user.full_name

    directory_users = f"./media/users_photo_id/{username}"

    if not os.path.exists(directory_users):
        os.makedirs(directory_users)

    await message.photo[-1].download(f"{directory_users}/{message.photo[-1].file_unique_id}.jpg")

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_view_photo = types.InlineKeyboardButton(text="Посмотреть фото", callback_data="view_photo")
    button_select_theme = types.InlineKeyboardButton(text="Выбор темы для стикерпака", callback_data="select_theme")

    keyboard.add(button_view_photo)
    keyboard.add(button_select_theme)

    await message.reply("Нажмите кнопку, чтобы посмотреть фото",
                        reply_markup=keyboard)

@dispatcher.callback_query_handler(lambda query: query.data == "view_photo")
async def view_photo(query: types.CallbackQuery):
    chat_id = query.from_user.id

    username = query.from_user.full_name
    directory = f"./media/users_photo_id/{username}"

    file_list = os.listdir(directory)
    photo = ""
    for file in file_list:
        photo = file

    image = types.InputFile(path_or_bytesio=f"{directory}/{photo}")

    await dispatcher.bot.send_photo(chat_id=chat_id, photo=image)
    await dispatcher.bot.send_message(chat_id=chat_id, text="Ваша фотография")

    os.remove(f"{directory}/{photo}")

@dispatcher.callback_query_handler(lambda query: query.data == "select_theme")
async def select_theme(query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    button_computer_technology = types.InlineKeyboardButton(text="Компьютерные технологии",
                                                            callback_data="computer_technology")
    button_emotions_and_expressions = types.InlineKeyboardButton(text="Эмоции и выражения",
                                                                 callback_data="emotions_and_expressions")
    button_phrases_and_memes = types.InlineKeyboardButton(text="Фразы и мемы",
                                                          callback_data="phrases_and_memes")

    keyboard.add(button_computer_technology)
    keyboard.add(button_emotions_and_expressions)
    keyboard.add(button_phrases_and_memes)

    await query.message.answer("Выберите тему для стикерпака", reply_markup=keyboard)

def get_user_data(fullname: str, theme: str, photo: str,
                  upload_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    user = UserData(full_name=fullname, photo_name=photo, upload_date=upload_date)
    json_data = json.dumps(user.__dict__, indent=4, separators=(", ", ": "))

    save_directory = f"json/{theme}{fullname}"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    file_name = f"{fullname}.json"
    file_path = f"{save_directory}/{file_name}"

    with open(file_path, "w") as file:
        file.write(json_data)

async def on_startup(dispatcher: Dispatcher):
    await on_startup_notify(dispatcher=dispatcher)
    await set_default_commands(dispathcer=dispatcher)
    print("Bot started")

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == "__main__":
    executor.start_polling(dispatcher=dispatcher,
                           on_startup=on_startup, on_shutdown=shutdown)
