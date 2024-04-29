from aiogram import Dispatcher, types

async def set_default_commands(dispathcer: Dispatcher):
    await dispathcer.bot.set_my_commands([
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="help", description="Помощь по боту")
    ])
