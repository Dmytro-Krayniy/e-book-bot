from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder, InlineKeyboardMarkup
from ..lexicon.lexicon import LEXICON
from ..services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for page in sorted(args):
        title = book[page][:100].replace('\n', ' ')
        kb_builder.row(InlineKeyboardButton(
            text=f'{page} - {title}',
            callback_data=str(page)
        ))
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks'),
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel'),
        width=2
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for page in sorted(args):
        title = book[page][:100].replace('\n', ' ')
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {page} - {title}',
            callback_data=f'{page}del'
        ))
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel'),
    )
    return kb_builder.as_markup()
