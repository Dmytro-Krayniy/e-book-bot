from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)
    config = Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
    # print(config.tg_bot)
    return config
