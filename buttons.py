from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

btn = [
    [types.KeyboardButton(text="Register️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
