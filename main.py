from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from aiogram import executor
from handlers import dispatcher

async def on_startup(dispatcher):
    await on_startup_notify(dispatcher=dispatcher)
    await set_default_commands(dispathcer=dispatcher)
    print('Bot started')

if __name__ == "__main__":
    executor.start_polling(dispatcher=dispatcher, on_startup=on_startup)
