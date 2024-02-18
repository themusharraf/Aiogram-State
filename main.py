import os
import logging
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message
from buttons import button

load_dotenv(".env")
TOKEN = os.getenv("Token")
Admin = os.getenv("Admin")
Channel = os.getenv("Channel")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)


class Form(StatesGroup):
    name = State()
    username = State()
    phone = State()
    finish = State()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Salom {message.from_user.full_name}", reply_markup=button)

    @router.message()
    async def starts(message: Message, state: FSMContext):
        if message.text == "Register️":
            await state.set_state(Form.name)
            await message.answer("Enter name")


@router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.username)
    await message.answer(f"Enter username {message.text}")


@router.message(Form.username)
async def process_username(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.set_state(Form.phone)
    await message.answer(f"Enter phone number")


@router.message(Form.phone)
async def process_username(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(phone=message.text)
    await state.set_state(Form.finish)
    data = await state.get_data()
    await state.clear()
    await message.answer(
        "You have successfully",
    )

    name = data.get("name", "Unknown")
    username = data.get("username", "Unknown")
    phone = data.get("phone", "Unknown")
    matn = f"Name: {name}\nPhone: {phone}\nUsername: {username}"
    await message.answer(matn)
    await bot.send_message(chat_id=Channel, text=matn)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", )
    asyncio.run(main())
