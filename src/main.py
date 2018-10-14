"""The bots essence"""
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
import time

"""Some setup"""
Clinet = discord.Client()
client = commands.Bot(command_prefix="!")

"""Default settings"""
bot_command_prefix = "!" #change this prefix to you liking

"""Events"""
@client.event
async def on_ready(): #executes when the bot is ready to process messages
    print("Bot is ready!")


"""Setup"""
print("Setup...")
config_file = open("../config/config.txt", "r")
config_file_content = config_file.read().split("\n")
config_file.close()
bot_cmd_prefix_defined = False #is the bot command defined in the config file
bot_token_defined = False #is the bot token defined in the config file
token = ""
for i in config_file_content:
    if i.startswith("bot-token:") and not bot_token_defined:
        token = "".join(i[10:].split(" "))
        bot_token_defined = True
    if i.startswith("bot-command-prefix:") and not bot_cmd_prefix_defined:
        bot_command_prefix = "".join(i[19:].split(" "))
        print("Using '"+bot_command_prefix+"' as bot command prefix")
        bot_cmd_prefix_defined = True

if not bot_token_defined:
    print("Error: Unspecified bot token! Please add it in config.txt")
    exit(0)

if not bot_cmd_prefix_defined:
    print("Warning: The bot command prefix is unspecified! Using the default '!'")


client.run(token)
