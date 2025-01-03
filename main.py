from src.build.creator import Creator
from src.build.loader import Loader
from src.build.launcher import Launch
import src.data.var, src.data.bot
from datetime import datetime
from src.utils.config import get_config

bot = src.data.bot.get_bot(get_config("TOKEN"), get_config("OWNER_ID"))

class main:
    def __init__(self):
        src.data.var.init_time(datetime.now())
        Creator()
        Loader(bot)
        Launch(bot)


if __name__ == '__main__':
    main()