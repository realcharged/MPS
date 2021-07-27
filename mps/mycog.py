import discord
from redbot.core import commands
from mcstatus import MinecraftServer
from discord.ext import tasks
import logging
import random
from typing import Literal
from dislash import *
from redbot.core.bot import Red
from redbot.core.config import Config
from discord_buttons_plugin import *
class MPS(commands.Cog):


    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def mpsvr(self, ctx):
        """Displays server status."""
        try:
            server = MinecraftServer.lookup("mps.modded.fun:25565")
            status = server.status()
            query = server.query()
            embed = discord.Embed(
                title=('MPSVR is currently Online'
                       '\n{0} players online'
                       '\nPlayer List:'
                       .format(status.players.online)),
                description=('{0}'.format(", ".join(query.players.names)))
            )
            embed.set_author(name='MPSVR Status')
            embed.set_footer(text='End of list')

            await ctx.send(embed=embed)


        except:
            embed = discord.Embed(
            title=('MPSVR is Offline'),
            description=('Yell at <@166311283744964608>!')
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def test(self, mps):
        """test"""
        embed = discord.Embed(title=('test'))
        await ctx.send(embed=embed)