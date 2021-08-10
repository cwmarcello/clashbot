# Attempt at a bot for organizing people for clash using slash commands

import discord
from dotenv import load_dotenv
import os
import random
import logging
import time

load_dotenv() # loads in environment variables from .env (for secrets)
client = discord.Client()

# Logging config
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='clashbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    this.days = [saturday, sunday]
    this.

@client.event
async def on_message(message):
    # don't send responses to yourself 
    if message.author == client.user:
        return


@bot.command()
async def signup(context, day, choice):
    