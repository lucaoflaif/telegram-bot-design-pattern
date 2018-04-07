"""Bot start file"""
import os
from env import ENV as env
from db import DB_CONNECTION
from core import Bot


if __name__ == "__main__":
    bot = Bot(env=env, db=DB_CONNECTION)
    bot.run()
