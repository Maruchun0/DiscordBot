import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

client = commands.Bot(command_prefix = 'sheesh ')
status_type = cycle([discord.ActivityType.playing, discord.ActivityType.listening])
status_name = cycle(["with ur mum XD", "dope a$$ music"])

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.playing, name="Coding, do not touch"))
    print('Bot ready')

@client.command()
async def info(ctx):
    await ctx.send(f'**Drip Charrier Bot**\nCreated by: *Sean BOGOSAVAC*\nV0.3 pre-Alpha')

@client.command()
async def lessgo(ctx):
    change_status.start()
    running = True
    await ctx.send(f'Drip Charrier in the place !')

@client.command()
async def holup(ctx):
    change_status.stop()
    running = False
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.playing, name="Coding, do not touch"))
    await ctx.send(f'Drip Charrier, out !')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

@tasks.loop(seconds=7)
async def change_status():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=next(status_type), name=next(status_name)))

client.load_extension(f'Cogs.basic')
client.run('ODUxNDUwNzI4NDQ5ODM1MDEy.YL4dSA.monlrUFVIzHNZ_pQZFtMxhfD0m4')
