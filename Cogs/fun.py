import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()    #Shows the cog is fully loaded
    async def on_ready(self):
        print('Fun Cog loaded')

    # Commands
    @commands.command() #Gives Drip Charrier's predictions
    async def DripCharrier(self, ctx, *, question):
        responses = ['Ouais', 'Nope', 'Fallait dripper plus que ça frère!']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command() #Gives a random famous Drip Charrier quote
    async def citation(self, ctx):
        Quotes = ["C'est un petit détail mais c'est avec les petits détails qu'on... voila quoi",
        "*Rire nerveux*",
        "Les maths, c'est beau quand même",
        "Et comme l'a dit un jour mon élève préféré, 'Celui qui a recopié l'exo, c'est vraiment un connard!'"]
        await ctx.send(f'**{random.choice(Quotes)}**\nDrip Charrier, out *Drop the mic*')


def setup(client):
    client.add_cog(Fun(client))
