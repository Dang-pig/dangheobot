# import libraries
from ast import Str
from http import client
import math
import random
import os
from pickle import TRUE
import string
from sys import prefix

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

from hmm import badwords
from hmm import says

# token and guild id
TOKEN = 'token'
GUILD = '1644971949559'

# set prefix
prefix = 'dh!'
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

class comm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='ping', aliases=['p'], help='Return a pong message!')
    async def ping_command(self, ctx):
        await ctx.send('Pong!')

from dhelp import c_help
bot.add_cog(c_help(bot))

# general commands
bot.add_cog(comm(bot))

# fun commands
from fun_comm import rps, dadjoke
bot.add_cog(rps(bot))
bot.add_cog(dadjoke(bot))

bot.run(TOKEN)

    # # get message content
    # mes = message.content.lower().split(' ')
    # command = mes[0]

    # elif(command == prefix + 'getinfo'): #command getinfo
    #     if len(mes) == 1: #if no argument return sender info
    #         us = message.author
    #         na = us.name
    #         jo = us.joined_at.strftime("%d/%m/%Y  %H:%M:%S")
    #         em = us.discriminator
    #         cr = us.created_at.strftime("%d/%m/%Y  %H:%M:%S")
    #         await message.channel.send(embed=discord.Embed(description='Name: **' + na + "#" + em + '** (a.k.a ' + str(us.display_name) + ')\n' + na + ' account created at: ' + cr + '\n' + na + ' server join time: ' + jo + '\n', color=0xffffff))
        
    #     elif len(mes) == 2: #if has argument return tagged user info
    #         tag = mes[1] #get tagged user

    #         if tag[2:-1] == str(message.author.id): #if tagged user is sender
    #             us = message.author
    #             na = us.name
    #             jo = us.joined_at.strftime("%d/%m/%Y  %H:%M:%S")
    #             em = us.discriminator
    #             await message.channel.send(embed=discord.Embed(description='Name: **' + na + "#" + em + '** (a.k.a ' + str(us.display_name) + ')\n' + 'Joined at: ' + jo + '\n', color=0xffffff))

    #         elif tag.startswith('<@'): #if tagged
    #             tag = tag[2:-1]
    #             i = int(tag)
    #             us = await self.fetch_user(i)
    #             na = str(us.name)
    #             de = str(us.discriminator)
    #             da = str(us.created_at.strftime("%d/%m/%Y  %H:%M:%S"))
    #             await message.channel.send(embed=discord.Embed(description="**" + na + "#" + de + "** (a.k.a " + str(us.display_name) + ")\nAccount created at: " + da, color=0xffffff))

    #         else: #if not tagged
    #             await message.channel.send("Please ping a user to getinfo!")

    # elif(command == prefix + 'getavatar'): #command getavatar
    #     if len(mes) == 1: #if no argument return sender avatar
    #         await message.channel.send(str(message.author.avatar_url))
    #     elif len(mes) == 2: #if has argument return tagged user avatar
    #         tag = mes[1]
    #         if tag[2:-1] == str(message.author.id):
    #             await message.channel.send(str(message.author.avatar_url))
    #         elif tag.startswith('<@'):
    #             tag = tag[2:-1]
    #             i = int(tag)
    #             us = await self.fetch_user(i)
    #             await message.channel.send(str(us.avatar_url))
    #         else:
    #             await message.channel.send("Please ping a user to getavatar!")
    # elif(command == prefix + 'play'):
    #     if len(mes) == 1:
    #         await message.channel.send("Please specify a song!")
    #     elif len(mes) == 2:
    #         song = mes[1]
    #         if not song.startswith('https://www.youtu'):
    #             await message.channel.send("Please specify a valid YouTube link!")
    # else: #if not command or wrong command
    #     c = [char for char in message.content]
    #     if (len(message.content) >= 3) and (c[0] + c[1] + c[2] == prefix):
    #         await message.channel.send('🤔 That\'s not a command!')
    #         if c[3] == 'p':
    #             await message.channel.send('Did you mean **dh!ping**?')
    #         elif c[3] == 'h':
    #             await message.channel.send('Did you mean **dh!help**?')
    #         elif c[3] == 'g':
    #             await message.channel.send('Did you mean **dh!getinfo** or **dh!getavatar**?')
    #         elif c[3] == 'r':
    #             await message.channel.send('Did you mean **dh!rps**?')
    #         elif c[3] == 'd':
    #             await message.channel.send('Did you mean **dh!dadjoke**?')
    #         else:
    #             pass
    #     else:
    #         con = False
    #         for x in range(len(badwords)):
    #             if message.content.lower().find(badwords[x]) != -1:
    #                 print("found " + badwords[x])
    #                 con = True
    #         if con == True:
    #             rand = random.randint(0, len(says) - 1)
    #             await message.channel.send(says[rand])

    # return