from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnHello = KeyboardButton("Привет, что ты умеешь?")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


button1 = KeyboardButton("Таблица патронов")
button2 = KeyboardButton("Оружие в мете")
button3 = KeyboardButton("Таблица брони")
button4 = KeyboardButton("Таблица шлемов")
button5 = KeyboardButton("Таблица рюкзаков")
button6 = KeyboardButton("Карты локаций")
button7 = KeyboardButton("Все боссы игры")

markup1 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(button7)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3, button4, button5, button6, button7)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3, button4, button5, button6, button7).add(KeyboardButton("На этом все"))