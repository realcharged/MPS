import discord
from redbot.core import commands
from mcstatus import MinecraftServer
from discord.ext import tasks
from redbot.core.bot import Red
from redbot.core.config import Config
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
    async def common(self, ctx):
        embed = discord.Embed()
        embed.add_field(name = 'Music cmds', value= "[prefix]play\n[prefix]now\n[prefix]skip\n[prefix]pause\n[prefix]stop", inline = True)
        embed.add_field(name = 'Extra cmds', value=
        ";mpsvr Server status of MPSVR."
        "\n;bday"
        "\n;uptime Total time bot has been up."
        "\n;rps Rock, paper, scissors."
        "\n;sticky Pins messages to bottom of channels."
        "\n;unsticky unPins messages."

        inline = False)

        embed.set_author(name='Common Commands')

        await ctx.send(embed=embed)
