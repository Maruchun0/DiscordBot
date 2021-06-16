import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = 'sheesh ')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.playing, name="with ice"))
    print('Bot ready')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

for file in os.listdir('./Cogs'):
    if file.endswith('.py'): client.load_extension(f'Cogs.{file[:-3]}')

client.run('ODUxNDUwNzI4NDQ5ODM1MDEy.YL4dSA.monlrUFVIzHNZ_pQZFtMxhfD0m4')
