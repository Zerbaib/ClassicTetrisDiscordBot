
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
    async def top(self, ctx, game: str = None, mode: str = None):
        if game is None:
            game = "CLASSIC"
        else:
            game = game.upper()
        if mode is None:
            mode = "NTCS"
        else:
            mode = mode.upper()
        
        if game not in ["CLASSIC", "TETRISGB", "TETRISN64", "TETRISDS"]:
            embed = disnake.Embed(
                title="Invalid game",
                description="This game doesn't exist in the database\n\n**Available games:**\n- Classic\n- TetrisGB\n- TetrisN64\n- TetrisDS",
                color=disnake.Color.brand_red()
            )
            await ctx.send(embed=embed)
            return
        if mode not in self.data[ctx.author.id]['GAME'][game]:
            for mode_avalable in self.data[ctx.author.id]['GAME'][game]:
                mode_avalable = [mode_avalable]
            embed = disnake.Embed(
                title="Invalid mode",
                description=f"This game doesn't exist in the database\n\n**Available mode:**\n{mode_avalable}",
                color=disnake.Color.brand_red()
            )
            await ctx.send(embed=embed)
            return
        for user_id in self.data():
            self.data[user_id]['GAME'][game][mode]
            pass
        pass

def setup(bot):
    bot.add_cog(Top(bot))
