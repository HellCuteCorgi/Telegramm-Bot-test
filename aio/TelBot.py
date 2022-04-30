from typing import Text
from config import TOKEN #Импорт API из файла config.
import logging
from aiogram import Bot, Dispatcher, executor, types #Импортируем все нужно нам из библеотеки AIOGram.
import keyboards as kb #Созданая кнопка в отдельном классе импортированная в main.

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#Первая команда для бота. Приветствие и информация о дальнейших действиях.
@dp.message_handler(commands=['start']) 
async def process_hello(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nЯ - бот-помощник по игре Escape From Tarkov. Но сначала нажми кнопку /reg, введи свой ник, чтобы я знал как к тебе обращаться и узнать, что я умею.", reply_markup=kb.greet_kb)

@dp.message_handler(lambda message: message.text =="Привет, что ты умеешь?")
async def with_puree(message: types.Message):
    await message.reply("Мои функции по команде /help ")

#Команда help помогает пользователю узнать о функциях бота
@dp.message_handler(commands=['help'])
async def process_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Вот мои функции: ", reply_markup=kb.markup3) 

@dp.message_handler()
async def process_help(message: types.Message):
    await message.reply(message.from_user.id, 'Вот мои возможности: ')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)