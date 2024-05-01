from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from aiogram import executor, Dispatcher, types
from handlers import dispatcher

from user_data import UserData

import json
from datetime import datetime

users_data = []
count_files_user = [1]

@dispatcher.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    # Получаем информацию о пользователе
    user = message.from_user

    # Получаем полное имя пользователя
    full_name = f"{user.full_name}"

    # Получаем название загруженной фотографии
    photo_name = message.photo[-1].file_id

    # Получаем дату загрузки фотографии
    upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Создаем экземпляр класса UserData
    user_data = UserData(f"{full_name}_{count_files_user[-1]}", photo_name, upload_date)

    users_data.insert(user_data)

    # Сериализуем объект UserData в JSON
    json_data = json.dumps(users_data[-1].__dict__, indent=4, separators=(", ", ": "))

    # Сохраняем JSON-файл в указанную директорию
    save_directory = "./json"
    filename = f"{full_name}_{users_data[-1]}.json"
    filepath = f"{save_directory}/{filename}"
    with open(filepath, "w") as file:
        file.write(json_data)

    count_files_user.insert(count_files_user[-1] + 1)
    
    # Отправляем пользователю сообщение о сохранении данных
    await message.reply("Ваши данные сохранены успешно!")

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
