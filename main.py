from datetime import datetime

import src.data.bot
import src.data.var
from src.build.creator import Creator
from src.build.executor import Executor
from src.build.launcher import Launch
from src.build.loader import Loader
from src.utils.config import get_config

bot = src.data.bot.get_bot(get_config("TOKEN"), get_config("OWNER_ID"))

class main:
    def __init__(self):
        src.data.var.init_time(datetime.now())
        Creator()
        Loader(bot)
        Executor()
        Launch(bot)


if __name__ == '__main__':
    main()