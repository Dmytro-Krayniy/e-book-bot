from aiogram import Bot
from aiogram.types import BotCommand

from rock_scissors_paper_bot.lexicon.lexicon_ru import LEXICON_COMMANDS_RU


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=com, description=desc) for com, desc in LEXICON_COMMANDS_RU.items()]
    await bot.set_my_commands(main_menu_commands)
