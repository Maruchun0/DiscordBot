import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()    #Shows the cog is fully loaded
    async def on_ready(self):
        print('Basic Cog loaded')

    # Commands
    @commands.command() #Shows the latency of the bot
    async def ping(self, ctx):
        await ctx.send(f'My ice only took {round(self.client.latency * 1000)} miliseconds to drip!')


def setup(client):
    client.add_cog(Basic(client))
