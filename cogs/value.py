
import disnake
from disnake.ext import commands
import json

class ValueCog(commands.Cog):
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

    @commands.slash_command(name="setvalue", description="Sets user value")
    async def setvalue(self, ctx, game: str = None, mode: str = None, value=int):
        try:
            if game is None:
                game = "CLASSIC"
            elif mode is None:
                mode = "NTSC"
            else:
                game = game.upper()
                mode = mode.upper()
                
            user_id = str(ctx.author.id)
            
            if game not in ["CLASSIC", "TETRISGB", "TETRISN64", "TETRISDS"]:
                embed = disnake.Embed(
                    title="Invalid game",
                    description="This game doesn't exist in the database\n\n**Available games:**\n- Classic\n- TetrisGB\n- TetrisN64\n- TetrisDS",
                    color=disnake.Color.brand_red()
                )
                await ctx.send(embed=embed)
                return
            if mode not in self.data[user_id]['GAME'][game]:
                await ctx.send("Invalid mode")
                return
            
            self.data[user_id]['GAME'][game][mode] = value
            with open(self.data_file, "w") as f:
                json.dump(self.data, f, indent=4)
            
            embed = disnake.Embed(
                title="Value set",
                description=f"**Game:** {game}\n**Mode:** {mode}\n**Value:** {value}",
                color=disnake.Color.brand_green()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"Error:\n\n```{e}```")

def setup(bot):
    bot.add_cog(ValueCog(bot))
