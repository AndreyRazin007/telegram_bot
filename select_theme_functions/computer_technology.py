from serialization.serialization_images import get_user_data

from aiogram import types

from handlers import dispatcher


@dispatcher.callback_query_handler(lambda query: query.data == "computer_technology")
async def sending_photos_computer_technology(query: types.CallbackQuery):
    photo_1 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_1.png")
    photo_2 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_2.png")
    photo_3 = types.InputFile(path_or_bytesio="./media/themes/computer_technology/image_3.png")

    album = types.MediaGroup()

    album.attach_photo(photo=photo_1)
    album.attach_photo(photo=photo_2)
    album.attach_photo(photo=photo_3)

    await query.message.answer_media_group(media=album)

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/computer_technology/image_1.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/computer_technology/image_2.png")

    get_user_data(fullname=query.from_user.full_name,
                        theme=query.data, photo="./media/themes/computer_technology/image_3.png")

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
