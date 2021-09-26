#  _   _            _                    _             _____ _____ 
#| | | |          | |                  | |           / __  |  _  |
#| |_| | ___ _ __ | |__   __ _  ___ ___| |_ _   _ ___`' / /| |/' |
#|  _  |/ _ | '_ \| '_ \ / _` |/ _ / __| __| | | / __| / / |  /| |
#| | | |  __| |_) | | | | (_| |  __\__ | |_| |_| \__ ./ /__\ |_/ /
#\_| |_/\___| .__/|_| |_|\__,_|\___|___/\__|\__,_|___\_____/\___/ 
#           | |                                                   
#           |_|                                                   
#______      _   _                  ______       _                
#| ___ \    | | | |                 | ___ \     | |               
#| |_/ _   _| |_| |__   ___  _ __   | |_/ / ___ | |_              
#|  __| | | | __| '_ \ / _ \| '_ \  | ___ \/ _ \| __|             
#| |  | |_| | |_| | | | (_) | | | | | |_/ | (_) | |_              
#\_|   \__, |\__|_| |_|\___/|_| |_| \____/ \___/ \__|             
#       __/ |                                                     
#      |___/   

import json
import os
import random
import discord
import sys
from discord.ext import tasks
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext



if not os.path.isfile("config.json"):
    sys.exit("'config.json' Bulunamıyor.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()





bot = Bot(command_prefix=config["bot_prefix"], intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print('bot aktif edildi')
    status_task.start()



@bot.event
async def on_message(message):
    # Ignores if a command is being executed by a bot or by the bot itself
    if message.author == bot.user or message.author.bot:
        return
    await bot.process_commands(message)

@tasks.loop(minutes=1.0)
async def status_task():
    statuses = [f"{config['bot_prefix']}help"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))

bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cmds"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cmds.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


@bot.event
async def on_slash_command(ctx: SlashContext):
    fullCommandName = ctx.name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Executed {executedCommand} command in {ctx.guild.name} (ID: {ctx.guild.id}) by {ctx.author} (ID: {ctx.author.id})")


@bot.event
async def on_command_error(context, error):
    raise error

bot.run(config["token"])