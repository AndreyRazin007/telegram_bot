from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from image_processing.processing import Processing
from serialization.serialization_images import get_user_data

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

@dispatcher.callback_query_handler(lambda query: query.data == "computer_technology")
async def sending_photos_computer_technology(query: types.CallbackQuery):
    source_photo_1 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_1.jpg")
    source_photo_2 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_2.jpg")
    source_photo_3 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_3.jpg")

    source_album = types.MediaGroup()
    source_album.attach_photo(photo=source_photo_1)
    source_album.attach_photo(photo=source_photo_2)
    source_album.attach_photo(photo=source_photo_3)

    await query.message.reply("Исходные фотографии темы:")

    await query.message.answer_media_group(media=source_album)

    username = query.from_user.full_name
    directory = f"./media/users_photo_id/{username}"

    file_list = os.listdir(directory)
    for file in file_list:
        photo = file
    
    processing = Processing()
    processing.save_swap_faces(f"{directory}/{photo}",
                               "./media/themes/computer_technology/image_1.png",
                               "computer_technology", "image_1.png")
    processing.save_swap_faces(f"{directory}/{photo}", "./media/themes/computer_technology/image_2.png",
                               "computer_technology", "image_2.png")
    processing.save_swap_faces(f"{directory}/{photo}", "./media/themes/computer_technology/image_3.png",
                               "computer_technology", "image_3.png")

    # await query.message.reply("Ваш стикерпак:")

    # sticker_1 = types.InputFile(path_or_bytesio="./media/save_users_stickers/computer_technology/image_1.jpg")
    # sticker_2 = types.InputFile(path_or_bytesio="./media/save_users_stickers/computer_technology/image_2.jpg")
    # sticker_3 = types.InputFile(path_or_bytesio="./media/save_users_stickers/computer_technology/image_3.jpg")

    # sticker_album = types.MediaGroup()
    # sticker_album.attach_photo(photo=sticker_1)
    # sticker_album.attach_photo(photo=sticker_2)
    # sticker_album.attach_photo(photo=sticker_3)

    # await query.message.answer_media_group(media=sticker_album)

    # get_user_data(fullname=f"{query.from_user.full_name}_1",
    #                     theme=query.data, photo="./media/themes/computer_technology/image_1.png")

    # get_user_data(fullname=f"{query.from_user.full_name}_2",
    #                     theme=query.data, photo="./media/themes/computer_technology/image_2.png")

    # get_user_data(fullname=f"{query.from_user.full_name}_3",
    #                     theme=query.data, photo="./media/themes/computer_technology/image_3.png")

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


@dispatcher.callback_query_handler(lambda query: query.data == "emotions_and_expressions")
async def sending_photos_emotions_and_expressions(query: types.CallbackQuery):
    photo_1 = types.InputFile(path_or_bytesio="./media/themes/emotions_and_expressions/image_1.png")
    photo_2 = types.InputFile(path_or_bytesio="./media/themes/emotions_and_expressions/image_2.png")
    photo_3 = types.InputFile(path_or_bytesio="./media/themes/emotions_and_expressions/image_3.png")

    album = types.MediaGroup()

    album.attach_photo(photo=photo_1)
    album.attach_photo(photo=photo_2)
    album.attach_photo(photo=photo_3)

    await query.message.answer_media_group(media=album)

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/emotions_and_expressions/image_1.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/emotions_and_expressions/image_2.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/emotions_and_expressions/image_3.png")

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


@dispatcher.callback_query_handler(lambda query: query.data == "phrases_and_memes")
async def sending_photos_phrases_and_memes(query: types.CallbackQuery):
    photo_1 = types.InputFile(path_or_bytesio="./media/themes/phrases_and_memes/image_1.png")
    photo_2 = types.InputFile(path_or_bytesio="./media/themes/phrases_and_memes/image_2.png")
    photo_3 = types.InputFile(path_or_bytesio="./media/themes/phrases_and_memes/image_3.png")

    album = types.MediaGroup()

    album.attach_photo(photo=photo_1)
    album.attach_photo(photo=photo_2)
    album.attach_photo(photo=photo_3)

    await query.message.answer_media_group(media=album)

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/phrases_and_memes/image_1.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/phrases_and_memes/image_2.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/phrases_and_memes/image_3.png")

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
