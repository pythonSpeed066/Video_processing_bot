from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot_token = os.getenv("bot_token")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот запущен!")


@dp.message_handler(commands=["start", "help"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_id, "Приветствие")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
