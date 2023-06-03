from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType

BOT_TOKEN: str = '6171738053:AAFUuJtnCfJw9GnuhdG0DAZpGEVTBB0mzl4'
TEXT1: str = 'Всі говорять: "'
TEXT2: str = '". \nА ти візьми та купи слона!'


bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def process_start_command(message: Message):
    await message.answer(f'Привіт, {message.from_user.first_name}!\n Купи слона!')


async def process_help_command(message: Message):
    await message.answer('Допоможу якщо купиш слона. :)')


@dp.message(Command(commands=['stop']))
async def process_stop_command(message: Message):
    await message.answer("Я втомився тебе вмовляти купити слона. :( \nПіду з'їм щось смачненьке. Бувай!")
    # dp.stop_polling()


async def send_photo_answer(message: Message):
    print('send_photo_answer')
    await message.reply_photo('https://cs8.pikabu.ru/post_img/big/2017/10/24/10/1508861434139454276.jpg')

async def send_voice_answer(message: Message):
    # print(message.voice.file_id)
    await message.reply_voice('AwACAgIAAxkBAANnZFJgw5aUwzZkJN-bnPNVch8ouLoAAjEqAAItOJFK4LKh7tmsn0YvBA')


# @dp.message(F.content_type == ContentType.TEXT)
async def reply(message: Message):
    await message.reply(f'{TEXT1}{message.text}{TEXT2}')


dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(process_stop_command, Command(commands=['stop']))
dp.message.register(send_photo_answer, F.photo)
dp.message.register(send_voice_answer, F.voice)
dp.message.register(reply)

if __name__ == '__main__':
    dp.run_polling(bot)
