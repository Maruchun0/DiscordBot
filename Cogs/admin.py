import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()    #Shows the cog is fully loaded
    async def on_ready(self):
        print('Admin Cog loaded')

    # Commands
    @commands.command() #Clears the 5 previous messages
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)

    @commands.command() #Kicks the selected user
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)

    @commands.command() #Bans the selected user
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'{member.mention} is not allowed to drip anymore!')

    @commands.command() #Unbans the selected user
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} is allowed to drip again!')
                return


def setup(client):
    client.add_cog(Admin(client))
