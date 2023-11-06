from disnake.ext import commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("🔩 /profile as been loaded")

    @commands.slash_command(name="profile", description="Shows user profile")
    async def profile(self, ctx, user = None):
        # Your code here
        pass

def setup(bot):
    bot.add_cog(Profile(bot))
