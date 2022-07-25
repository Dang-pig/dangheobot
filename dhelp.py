import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

import os

prefix = 'dh!'

# help command
class c_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='dhelp', aliases=['h'], help='Get help on commands!')
    async def help_command(self, ctx, *, command=None):
        h = 'prefix is **' + prefix + '**\n' + '''
        --GENERAL COMMAND--
        **1. ping** or p
        Return a pong message!
        **2. dhelp** or h
        Return this help message!
        **3. dadjoke** or dj
        Return a random dad joke!
        **4. rps** (syntax: `rps [rock, paper, scissors]`) or r
        Choose rock, paper or scissors and play with me!

        --MUSIC COMMAND--
        **5. play** (syntax: `play [song name]`)
        Play a song from YouTube!
        **6. pause**
        Pause the current song!
        **7. resume**
        Resume the current song!
        **8. stop**
        Stop and clear the current queue!
        **9. queue**
        Return the current queue!
        **10. skip**
        Skip the current song!
        '''
        await ctx.send(embed = discord.Embed(title = 'Help', description = h, color = 0xffffff))