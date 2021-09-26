from datetime import datetime, time
from enum import auto
from typing import Text
import discord
from discord import user
from discord import message
from discord.ext import commands
import os
import sys
import json
from discord.utils import time_snowflake

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




class HelpfulCommands2(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["help", "h"])
    async def yardım(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author

        message = discord.Embed(title="Yardım Menüsü")
        message.add_field(name='**Kategoriler**',value="<:cModerasyon:891412950416515083> **!Moderasyon**\n<a:cEglence:891412953662906438> **!Eğlence**", inline=False)


        await ctx.send(embed=message)

    @commands.command(aliases=["mod", "moderation", "moderasyon"])
    async def yardımmod(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author

        message = discord.Embed(title=(f"{message_TR['moderationmenutitle']}"))
        discord.Embed(title="123")
        message.add_field(name=(f"{message_TR['moderationmenu']}"), value=(f"**{config['bot_prefix']}Küfür-engel** | {message_TR['kufurengel_desc']}"), inline=False)


        await ctx.send(embed=message)

def setup(client):
    client.add_cog(HelpfulCommands2(client))
    