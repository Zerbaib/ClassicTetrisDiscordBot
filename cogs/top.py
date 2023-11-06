
import disnake
from disnake.ext import commands
import json

class Top(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data_file = "data.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    @commands.command()
    async def top(self, ctx, game: str = None):
        if game is None:
            game = "CLASSIC"
        else:
            game = game.upper()
        if game not in ["CLASSIC", "TETRISGB", "TETRISN64", "TETRISDS"]:
            embed = disnake.Embed(
                title="Invalid game",
                description="This game doesn't exist in the database\n\n**Available games:**\n- Classic\n- TetrisGB\n- TetrisN64\n- TetrisDS",
                color=disnake.Color.brand_red()
            )
            await ctx.send(embed=embed)
            return
        
        pass

def setup(bot):
    bot.add_cog(Top(bot))
