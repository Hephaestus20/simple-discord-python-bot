from datetime import datetime, time
from typing import Text
import discord
from discord.ext import commands
from discord.utils import time_snowflake


class HelpfulCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ava", "avatarm"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:member=ctx.message.author

        message = discord.Embed(title=(f"{member} <a:cTaDa:891407983391703110>"), color=discord.Colour.orange())
        message.set_image(url=member.avatar_url)
        message.set_footer(text=f"Sorgulayan: {member}")

        await ctx.send(embed=message)


def setup(client):
    client.add_cog(HelpfulCommands(client))