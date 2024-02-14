from aiogram.types import Message, URLInputFile
from aiogram import Bot
import requests

from .keyboards import getVideoBtn
from .local_setting import API_HOST

async def getMovie(message: Message):
    id = message.text

    response = requests.get(f'{API_HOST}/api/getmovie/{id}')
    if response.status_code == 404:

        response = 'Not found 404'
        await message.answer(response)