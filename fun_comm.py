from distutils.cmd import Command
from sys import prefix
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

import os
import random
import dadjokes

prefix = 'dh!'

class rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rps', aliases=['r'], help='Choose rock, paper or scissors and play with me!')
    async def rps_command(self, ctx, *, choice):
        if choice == None:
            await ctx.send('Please choose `rock, paper or scissors` (or `1, 2, 3` or `r, p, s`)!')
        else:
            if choice == 'rock' or choice == '1' or choice == 'r':
                uc = 'rock'
                u = 1
            elif choice == 'paper' or choice == '2' or choice == 'p':
                uc = 'paper'
                u = 2
            elif choice == 'scissors' or choice == '3' or choice == 's':
                uc = 'scissors'
                u = 3
            else:
                await ctx.send('Please choose avalid choice (`rock, paper or scissors`  or  `1, 2, 3`  or  `r, p, s`)!')
                return
            c = random.randint(1, 3)
            if c == 1:
                cc = 'rock'
            elif c == 2:
                cc = 'paper'
            else:
                cc = 'scissors'
            if u == c:
                s = 'You and I both chose **' + uc + '**! It\'s a tie!'
                await ctx.send(embed = discord.Embed(title = 'RPS', description = s, color = 0xffffff))
            elif u == 1 and c == 3:
                s = 'You chose **' + uc + '**\n' + 'I chose **' + cc + '**\n' + '**You win!**'
                await ctx.send(embed = discord.Embed(title = 'Result', description = s, color = 0xffffff))
            elif u > c:
                s = 'You chose **' + uc + '**\n' + 'I chose **' + cc + '**\n' + '**You win!**'
                await ctx.send(embed = discord.Embed(title = 'Result', description = s, color = 0xffffff))
            else:
                s = 'You chose **' + uc + '**\n' + 'I chose **' + cc + '**\n' + '**I win!**'
                await ctx.send(embed = discord.Embed(title = 'Result', description = s, color = 0xffffff))

class dadjoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='dadjoke', aliases=['dj'], help='Return a random dad joke!')
    async def dadjoke_command(self, ctx):
        await ctx.send(dadjokes.get_joke())