from aiogram import Router
from aiogram.types import Message

from rock_scissors_paper_bot.lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
