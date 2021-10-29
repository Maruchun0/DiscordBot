import discord
from discord.ext import commands, tasks
from itertools import cycle

# Variables
client = commands.Bot(command_prefix = 'sheesh ')
status_type = cycle([discord.ActivityType.playing, discord.ActivityType.listening])
status_name = cycle(["with ur mum XD", "dope a$$ music"])

# Functions
def is_me(ctx): #Checks if I am the typer of the command
    return ctx.author.name == "Maruchun" and ctx.author.discriminator == "6969"

# Events
@client.event   #Initializes the bot
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.playing, name="Coding, do not touch"))
    print('Bot ready')

@client.event   #Returns error if the command does not exist
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Cette commande n'existe pas *rire nerveux*")

# Commands
@client.command()   #Give info about the bot
async def info(ctx):
    await ctx.send(f'**Drip Charrier Bot**\nCreated by: *Sean BOGOSAVAC*\nV0.5 pre-Alpha')

@client.command()   #Switch the bot to ready mode
@commands.check(is_me)
async def lessgo(ctx):
    change_status.start()
    running = True
    await ctx.send(f'Drip Charrier in the place !')

@client.command()   #Switch the bot to working mode
@commands.check(is_me)
async def holup(ctx):
    change_status.stop()
    running = False
    await client.change_presence(status = discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.playing, name="Coding, do not touch"))
    await ctx.send(f'Drip Charrier, out !')

@client.command()   #Loads a cog
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()   #Unloads a cog
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

# Loops
@tasks.loop(seconds=7)  #Status loop
async def change_status():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=next(status_type), name=next(status_name)))

#Runs the bot
client.load_extension(f'Cogs.basic')
token = open("token.txt", 'r').read()
client.run(token)
