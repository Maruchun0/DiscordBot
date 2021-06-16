import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot activated')

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My ice only took {round(bot.latency * 1000)} miliseconds to drip!')

def setup(client):
    client.add_cog(Example(client))
