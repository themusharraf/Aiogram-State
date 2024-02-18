from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

btn = [
    [types.KeyboardButton(text="Register️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btn2 = [
    [types.KeyboardButton(text="salom 1"), types.KeyboardButton(text="salom 2")]
]
btn3 = types.ReplyKeyboardMarkup(keyboard=btn2, resize_keyboard=True)
