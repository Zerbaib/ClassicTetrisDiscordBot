import disnake
from disnake.ext import commands
from src.utils.config import get_config
from src.utils.logger import Log


class Launch:
    def __init__(self, bot):
        self.bot = bot
        self.setup_events()
        self.start()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            Log.info('------')
            Log.info(f'On {len(self.bot.guilds)} guilds')
            Log.info(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
            Log.info('------')

    def start(self):
        try:
            self.bot.run(get_config("TOKEN"))
        except Exception as e:
            Log.error("Failed to start bot")
            Log.error(e)
            exit()