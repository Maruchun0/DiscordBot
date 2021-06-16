import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = 'sheesh ')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')

@client.event
async def on_memeber_join(member):
    print(f'{member} is here to drip')

@client.event
async def on_member_remove(member):
    print(f'{member} did not have enough ice to stay here')

@client.command(aliases=['DripCharrier'])
async def _8ball(ctx, *, question):
    responses = ['Ouais', 'Nope', 'Fallait dripper plus que ça frère!']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def citation(ctx):
    Quotes = ["C'est un petit détail mais c'est avec les petits détails qu'on... voila quoi",
    "*Rire nerveux*",
    "Les maths, c'est beau quand même",
    "Et comme l'a dit un jour mon élève préféré, 'Celui qui a recopié l'exo, c'est vraiment un connard!'"]
    await ctx.send(f'**{random.choice(Quotes)}**\nDrip Charrier, out *Drop the mic*')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} is not allowed to drip anymore!')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.name}#{user.discriminator} is allowed to drip again!')
            return

for file in os.listdir('./Cogs'):
    if file.endswith('.py'): client.load_extension(f'Cogs.{file[:-3]}')

client.run('ODUxNDUwNzI4NDQ5ODM1MDEy.YL4dSA.monlrUFVIzHNZ_pQZFtMxhfD0m4')
