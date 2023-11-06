import json
import disnake
from disnake.ext import commands

class ProfileCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def load_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    def save_data(self, data):
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        print("🔩 /profile as been loaded")

    @commands.slash_command(name="profile", description="Shows user profile")
    async def profile(self, ctx, user: disnake.User = None):
        data = self.load_data()
        if user == None:
            user = ctx.author
        
        user_id = str(user.id)
        
        if user_id not in data:
            embed = disnake.Embed(
                title="User not found",
                description="This user doesn't have a profile",
                color=disnake.Color.brand_red()
            )
            embed.set_footer(icon_url=user.avatar.url, text=f"Ececuted by {user}")
            await ctx.send(embed=embed)
            return

        embed = disnake.Embed(
            title=f"{user.display_name}'s profile",
            description=f"**Username:** {data[user_id]['USERNAME']}\n**Playstyle:** {data[user_id]['PLAYSTYLE']}\n**Country:** {data[user_id]['COUNTRY']}\n**Same Piece Set:** {data[user_id]['SAMEPIECESET']}",
            color=disnake.Color.brand_green()
        )
        embed.add_field(name="Classic Tetris", value=f"**NTSC:** {data[user_id]['GAME']['CLASSIC']['NTSC']}\n**NTSC (19):** {data[user_id]['GAME']['CLASSIC']['NTSC (19)']}\n**PAL:** {data[user_id]['GAME']['CLASSIC']['PAL']}\n**PAL (19):** {data[user_id]['GAME']['CLASSIC']['PAL (19)']}", inline=False)
        embed.add_field(name="Tetris GB", value=f"**NTSC:** {data[user_id]['GAME']['TETRISGB']['NTSC']}\n**NTSC (19):** {data[user_id]['GAME']['TETRISGB']['NTSC (19)']}\n**PAL:** {data[user_id]['GAME']['TETRISGB']['PAL']}\n**PAL (19):** {data[user_id]['GAME']['TETRISGB']['PAL (19)']}", inline=False)
        embed.add_field(name="Tetris N64", value=f"**NTSC:** {data[user_id]['GAME']['TETRISN64']['NTSC']}\n**Sprint:** {data[user_id]['GAME']['TETRISN64']['SPRINT']}\n**Marathon:** {data[user_id]['GAME']['TETRISN64']['MARATHON']}\n**Ultra:** {data[user_id]['GAME']['TETRISN64']['ULTRA']}", inline=False)
        embed.add_field(name="Tetris DS", value=f"**NTSC:** {data[user_id]['GAME']['TETRISDS']['NTSC']}\n**NTSC (19):** {data[user_id]['GAME']['TETRISDS']['NTSC (19)']}\n**PAL:** {data[user_id]['GAME']['TETRISDS']['PAL']}\n**PAL (19):** {data[user_id]['GAME']['TETRISDS']['PAL (19)']}", inline=False)
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(icon_url=user.avatar.url, text=f"Ececuted by {user}")
        await ctx.send(embed=embed)
        pass
    
    @commands.slash_command(name="setprofile", description="Sets user profile")
    async def setprofile(self, ctx):
        data = self.load_data()
        user = ctx.author
        
        if user.id in data:
            embed = disnake.Embed(
                title="You already have a profile",
                description="You can use `/profile` to see your profile",
                color=disnake.Color.brand_red()
            )
            embed.set_footer(icon_url=user.avatar.url, text=f"Ececuted by {user}")
            await ctx.send(embed=embed)
            return
        
        stats = {
                "USERNAME": user.name,
                "AVATAR": user.avatar.url,
                "PLAYSTYLE": None,
                "COUNTRY": None,
                "SAMEPIECESET": None,
                "GAME": {
                    "CLASSIC": {
                        "NTSC": None,
                        "NTSC (19)": None,
                        "PAL": None,
                        "PAL (19)": None
                    },
                    "TETRISGB": {
                        "NTSC": None,
                        "NTSC (19)": None,
                        "PAL": None,
                        "PAL (19)": None
                    },
                    "TETRISN64": {
                        "NTSC": None,
                        "SPRINT": None,
                        "MARATHON": None,
                        "ULTRA": None
                    },
                    "TETRISDS": {
                        "NTSC": None,
                        "NTSC (19)": None,
                        "PAL": None,
                        "PAL (19)": None
                    }
                    }
                }
        
        data[user.id] = stats
        self.save_data(data)

        embed = disnake.Embed(
            title="Your profile has been set",
            description=f"You can now use `/profile` to see your profile\nTo set values, use `/setvalue <value> <value>`",
            color=disnake.Color.brand_green()
        )
        embed.set_footer(icon_url=user.avatar.url, text=f"Ececuted by {user}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ProfileCog(bot))
