from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..lexicon.lexicon import LEXICON


def create_pagination_keyboard(current_page: int, total_pages: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons = ['backward' if current_page > 1 else '',
               f'{current_page}/{total_pages}',
               'forward' if current_page < total_pages else '']
    kb_builder.row(*[InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button,
                                          callback_data=button) for button in buttons if button != ''])
    return kb_builder.as_markup()
