import os

from src.data.var import folders
from src.utils.logger import Log


class Loader():
    def __init__(self, bot):
        self.bot = bot
        self.load_events()
        self.load_cogs()

    def load_events(self):
        for element in os.listdir(folders['events']):
            Log.log(f"Loading {element}")
            try:
                if element.endswith(".py"):
                    eventName = element[:-3]
                    try:
                        self.bot.load_extension(f'src.events.{eventName}')
                        Log.info(f"Loaded {element}")
                    except Exception as e:
                        Log.error(f"Failed to load {element}")
                        Log.error(e)
                        exit()
            except Exception as e:
                Log.error(f"Failed to load {element}")
                Log.error(e)
                exit()
    def load_cogs(self):
        for element in os.listdir(folders['cogs']):
            Log.log(f"Loading {element}")
            try:
                elementDir = f"{folders['cogs']}{element}"
                if os.path.isdir(elementDir):
                    for filename in os.listdir(elementDir):
                        Log.log(f"Loading {filename}")
                        if filename.endswith(".py"):
                            cogName = filename[:-3]
                            try:
                                self.bot.load_extension(f'src.modules.{element}.{cogName}')
                                Log.info(f"Loaded {filename}")
                            except Exception as e:
                                Log.error(f"Failed to load {filename}")
                                Log.error(e)
                                exit()
            except Exception as e:
                Log.error(f"Failed to load {element}")
                Log.error(e)
                exit()