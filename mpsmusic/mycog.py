import discord
from redbot.core import commands


class mpsmusic(commands.Cog):


    """My custom cog"""

    def __init__(bot):
        self.bot = bot
    @commands.command()
    async def play(ctx, self):
        embed = discord.Embed(
            title="Temp Resonse",
            description=("this is a temp response for the" (prefix) " command")
        )
        await ctx.send 
