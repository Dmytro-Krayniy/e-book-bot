import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from rock_scissors_paper_bot.keyboards.set_menu import set_main_menu


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logging.info('Starting bot')
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    # dp.startup.register(set_main_menu)
    await set_main_menu(bot)
    # await bot.delete_my_commands()   # For deleting menu button from bot
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
