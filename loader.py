from aiogram import Bot, Dispatcher, types

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)