import disnake
from disnake.ext import commands


def get_bot(prefix: str, ownerID: int):
    bot = commands.Bot(
        command_prefix=prefix,
        intents=disnake.Intents.all(),
        case_insensitive=True,
        owner_id=ownerID
    )
    return bot