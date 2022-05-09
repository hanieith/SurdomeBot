from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from parser import Parser

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def star_message(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           'Привет, это словарь языка жестов SurdoMe, напиши мне слово которое ты хочешь увидеть на языке жестов')


@dp.message_handler()
async def echo_message(msg: types.Message):
    pars = Parser(msg.text)
    await bot.send_message(msg.from_user.id, pars.get_link())


if __name__ == '__main__':
    executor.start_polling(dp)
