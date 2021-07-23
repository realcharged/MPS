import discord
from redbot.core import commands
from mcstatus import MinecraftServer
from discord.ext import tasks

class MPS(commands.Cog):

    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mpsvr(self, ctx):
        """Displays server status."""
        server = MinecraftServer.lookup("mps.modded.fun:25565")
        status = server.status()
        query = server.query()
        embed = discord.Embed(
            title=('This server is currently <online/offline>'
                   '\n{0} players online'
                   '\nPlayer List:'
                   .format(status.players.online)),
            description=('{0}'.format(", ".join(query.players.names)))
        )
        embed.set_author(name='MPSVR Status')
        embed.set_footer(text='End of list')

        await ctx.send(embed=embed)
