# Attempt at a bot for organizing people for clash using slash commands

import discord
from dotenv import load_dotenv
import logging

import os
import random


from enum import Enum
import copy

import datetime
from dateutil import tz
import time


load_dotenv() # loads in environment variables from .env (for secrets)
client = discord.Client()

# Logging config
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='clashbot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Global Variables
commands = ["/create_event", "/signup", "/make_team", "/list_players", "/info", ]
events = []

class Rank(Enum):
    Unranked = 0
    BronzeIV = 1
    BronzeIII = 2
    BronzeII = 3
    BronzeI = 4
    SilverIV = 5
    SilverIII = 6
    SilverII = 7
    SilverI = 8
    GoldIV = 9
    GoldIII = 10
    GoldII = 11
    GoldI = 12
    PlatinumIV = 13
    PlatinumIII = 14
    PlatinumII = 15
    PlatinumI = 16
    DiamondIV = 17
    DiamondIII = 18
    DiamondII = 19
    DiamondI = 20
    Masters = 21
    Challenger = 22

class Role(Enum):
    Top = 1
    Jungle = 2
    Mid = 3
    ADC = 4
    Support = 5

'''
def checkDateTime(year, month, day, hour, minute):
    try:
        date = datetime.datetime(
            year=year, 
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            tzinfo=timezone
        )
        return date 
    except:
        return None
'''

def createDatetime(datestr):
    date = datetime.fromisoformat(datestr)
    return date

def createEvents(datestr):
    date = createDate(datestr)
    event = new Event(date)

class Event:
    def __init__(self, date):
        date = date
        availables = []
        unavailables = []
        tentatives = []
        team = {}

        # a dictionary of lists, with each list consisting of the players who can play that role
        roles = {} 
        for role in list(Role):
            roles[role] = []

    def add_available_player(player):
        # add to available, roles
        self.availables.append(player)
        for role in player.roles:  # for every role the player can play
            self.roles[role].append(player) # add them to the event's list of roles

        # removal from everywhere else
        if player in self.unavailables:
            self.unavailables.remove(player)
        if player in self.tentatives:
            self.tentatives.remove(player)

        
    def add_unavailable_player(player):
        # add to tentative
        self.unavailables.append(player)
        
        # removal from everywhere else
        if player in self.availables:
            self.availables.remove(player)
        if player in self.tentatives:
            self.tentatives.remove(player)
        for role in list(self.roles):
            if player in self.roles[role]:
                self.roles[role].remove(player)
        if player in self.team:
            self.team.remove(player)

    def add_tentative_player(player):
        # add to tentative
        self.tentatives.append(player)
        
        # removal everywhere else
        if player in self.availables:
            self.availables.remove(player)
        if player in self.unavailables:
            self.unavailables.remove(player)   
        for role in list(self.roles):
            if player in self.roles[role]:
                self.roles[role].remove(player)
        if player in self.team:
            self.team.remove(player)

    def list_players():
        available_string = "The following players are signed up:\n"
        available_string += f"{player}\n" for player in self.availables
        unavailable_string = "The following players are signed up:\n"
        unavailable_string += f"{player}\n" for player in self.unavailables
        tentatives_string = "The following players are signed up:\n"
        tentatives_string += f"{player}\n" for player in self.tentatives
        players_string = available_string + unavailable_string + tentatives_string
        return players_string
    
    def make_team():
        local_roles = copy.deepcopy(self.roles)
        tentative_team = {}
        
        # Check for empty or unique roles to make an easy team
        for i in range(len(5)):
            for role in list(local_roles):
                if local_roles[role].length < 1:
                    return None # no one plays the role, there's not an easy team. exit
                if local_roles[role].length == 1: # only one person plays a role, add them
                    player = local_roles[role].pop() 
                    tentative_team[role] = player 

                    for role in local_roles: # remove them from all other roles
                        if player in role:
                            role.remove(player)

        # TODO: More complex team generation?

        self.team = tentative_team
        return tentative_team
            

class Player:
    def __init__(self):
        roles = []
        rank = Rank.Unranked
        clash_tier = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # don't send responses to yourself 
    if message.author == client.user:
        return

    # check if the bot is mentioned, if so, check for commands, if not, return
    for role in message.role_mentions:
        if "clashbot" in role.name.lower():
            command, args = parse_chat_command(message)
            if command:
                handle_command(message, command, args)
            else:
                return
        else:
            return
    
    elif ("signup" or "sign_up") in message.content():


# ensures that a command is a valid command (in the list), otherwise send a help message
def check_chat_command(message):
    for command in commands:
        if command in message.content():
            before, cmd_text, after = message.content.partition(command)
            args = after.split(" ")
            return command, args
        else:
            await message.channel.send("Command not found. Send '@clashbot /info` for command listing and more info")
            return None
    
# routes commands to the correct methods 
# message: message object
# command: command str
# args: list of strings

# TODO: Pickup here with command parsing and management

def handle_command(message, command, args):
    if command == "/create_event":
        date_obj = createDate(args[0])
        events.add(Event(date))

    if command == ""