"""The bots essence"""
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
import time

"""Some setup"""
Clinet = discord.Client()
client = commands.Bot(command_prefix="!") #this command_prefix is not used the command prefix should be defined in the variable below

"""Constants"""
bot_command_prefix = "!" #change this prefix to you liking
token = "" #enter your token here

@client.event
async def on_ready(): #executes when the bot is ready to process messages
    print("Bot is ready!")


client.run(token)
