import discord
from discord.ext import commands
import os
import sys
import json

if not os.path.isfile("config.json"):
    sys.exit("'config.json' Bulunamıyor.")
else:
    with open("config.json") as file:
        config = json.load(file)

if not os.path.isfile("lang\.\message_TR.json"):
    sys.exit("'message_TR.json' Bulunamıyor.")
else:
    with open("lang\.\message_TR.json", encoding='utf8') as file:
        message_TR = json.load(file)




class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["küfür-engel"])
    async def küfürengel(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author

        message = discord.Embed()
        message.add_field(name=(f"{message_TR['kufurengel_titleerror']}"),value=(f"{message_TR['kufurengel_error']}"), inline=False)


        await ctx.send(embed=message)

        


def setup(client):
    client.add_cog(ModerationCommands(client))
    