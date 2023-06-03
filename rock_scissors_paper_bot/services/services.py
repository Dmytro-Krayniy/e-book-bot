from random import choice

from ..lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice() -> str:
    return choice(['rock', 'scissors', 'paper'])


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


def get_winner(user_choice, bot_choice) -> str:
    user_choice = _normalize_user_answer(user_choice)
    if user_choice == bot_choice:
        return 'nobody_won'
    if (user_choice, bot_choice) in [('rock', 'scissors'),
                                     ('scissors', 'paper'),
                                     ('paper', 'rock')]:
        return 'user_won'
    else:
        return 'bot_won'
