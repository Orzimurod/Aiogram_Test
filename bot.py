import asyncio
import logging
import sys
from os import getenv

from aiogram import F, Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from utils import calculate
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7631118222:AAEgGIr5KMtOijATCwlnZbyfYsiOgg_4lz0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Tabriknomalar")]], resize_keyboard=True)
    await message.answer(f"Assalom alaykum.\nQuyidagi kerakli bo'limlarni yanlang!", reply_markup=keyboard)


@dp.message(F.text == "Tabriknomalar")
async def command_start_handler(message: Message):
        keyboard = ReplyKeyboardMarkup(
             keyboard=[[KeyboardButton(text="Bayramlar"), KeyboardButton(text="Tug'ilgan kun")],
                       [KeyboardButton(text="To'y"), KeyboardButton(text="Yubiley")]], resize_keyboard=True)
        await message.answer(f"Nima bilan Tabriklamoqchisiz?", reply_markup=keyboard)


@dp.message(F.text == "Bayramlar")
async def command_start_handler(message: Message):
        keyboard = ReplyKeyboardMarkup(
             keyboard=[[KeyboardButton(text="Qurbon hayiti"), KeyboardButton(text="Yangi yil")],
                       [KeyboardButton(text="Navruz Bayrami"), KeyboardButton(text="Bolalar kuni")]], resize_keyboard=True)
        await message.answer(f"Bayramlarni Tanlang", reply_markup=keyboard)


@dp.message(F.text == "Yangi yil")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Qurbon hayiti")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Navruz bayrami")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Bolalar kuni")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Tug'ulgan kun")
async def command_start_handler(message: Message):
        keyboard = ReplyKeyboardMarkup(
             keyboard=[[KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")],
                       [KeyboardButton(text="Qizaloq"), KeyboardButton(text="Bolakay")]], resize_keyboard=True)
        await message.answer(f"Kimga ekanini tanlang!", reply_markup=keyboard)

@dp.message(F.text == "Erkak")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Ayol")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Qizaloq")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Bolakay")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "To'y")
async def command_start_handler(message: Message):
        keyboard = ReplyKeyboardMarkup(
             keyboard=[[KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")]], resize_keyboard=True)
        await message.answer(f"Kimga ekanini tanlang!", reply_markup=keyboard)

@dp.message(F.text == "Erkak")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Ayol")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Yubiley")
async def command_start_handler(message: Message):
        keyboard = ReplyKeyboardMarkup(
             keyboard=[[KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")]], resize_keyboard=True)
        await message.answer(f"Kimga ekanini tanlang!", reply_markup=keyboard)

@dp.message(F.text == "Erkak")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


@dp.message(F.text == "Ayol")
async def command_start_handler(message: Message):
         await message.answer(f"Tabrik so'z tayyorlanmoqda")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())