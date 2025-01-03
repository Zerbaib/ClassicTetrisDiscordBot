import disnake
from disnake.ext import commands
from src.utils.saver import Saver
from src.utils.logger import Log
from src.utils.error import error_embed as error

class TopNtsc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        Log.info("🔩 '/top ntsc' has been loaded")

    @commands.slash_command(name="top_ntsc", description="Get the top 10 NES tetris high scores")
    async def top_ntsc(self, inter):
        try:
            await inter.response.defer()
            users = Saver.get_top("ntsc", "pb", 10)
            embed = disnake.Embed()
            embed.title = "🔝 Top 10 NES Tetris High Scores"
            embed.color = disnake.Color.blurple()
            if not users:
                embed.description = "No high scores found"
            else:
                for user in users:
                    user_id = user[1]
                    user_pb = user[2]
                    try:
                        user_name = await self.bot.fetch_user(user_id)
                    except:
                        user_name = "Unknown"
                    title = f"# {users.index(user) + 1} - {user_name}"
                    text = f"Score: {user_pb}"
                    embed.add_field(name=title, value=text, inline=False)

            await inter.edit_original_message(embed=embed)
            Log.log("🔝 Top 10 NES Tetris High Scores")
        except Exception as e:
            Log.error("An error occured while executing /top ntsc command")
            Log.error(e)
            await inter.send(embed=error(e))

def setup(bot):
    bot.add_cog(TopNtsc(bot))