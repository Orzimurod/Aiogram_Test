import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Router
from aiogram.fsm.context import FSMContext
from sessions import register_customer
from states.register import RegisterForm
from utils import get_word


register_router = Router()


@register_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(RegisterForm.lang)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🇺🇿 O'zbek tili"), KeyboardButton(text="🇷🇺 Rus tili")]], resize_keyboard=True)

    await message.answer(f"Assalomu alaykum.\nKerakli tilni tanlang!", reply_markup=keyboard)


@register_router.message(RegisterForm.lang)
async def lang_handler(message: Message, state: FSMContext) -> None:
    if message.text == "🇺🇿 O'zbek tili":
        await state.set_data({'lang': 'uz'})
    elif message.text == "🇷🇺 Rus tili":
        await state.set_data({'lang': 'ru'})
    data = await state.get_data()
    await state.set_state(RegisterForm.name)


    await message.answer(await get_word('name', data['lang']), reply_markup=ReplyKeyboardRemove())


@register_router.message(RegisterForm.name)
async def lang_handler(message: Message, state: FSMContext) -> None:
    await state.update_data({'name': message.text})
    data = await state.get_data()
    await state.set_state(RegisterForm.phone)


    await message.answer(await get_word('phone', data['lang']))


@register_router.message(RegisterForm.phone)
async def name_handler(message: Message, state: FSMContext) -> None:
    await state.update_data({'phone': message.text})
    data = await state.get_data()
    await state.set_state(RegisterForm.company)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=await get_word('skip', data['lang']))]], resize_keyboard=True)

    await message.answer(await get_word('company', data['lang']), reply_markup=keyboard)


@register_router.message(RegisterForm.company)
async def company_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not message.text == await get_word('skip', data['lang']):
        await state.update_data({'company': message.text})
    await register_customer(state)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=await get_word('tabriknomalar', data['lang'])),
                   KeyboardButton(text=await get_word('devor', data['lang']))]],
        resize_keyboard=True)
    await state.clear()

    await message.answer(await get_word('registered', data['lang']), reply_markup=keyboard)