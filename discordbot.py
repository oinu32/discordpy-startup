import discord
import re
import os
import traceback
import random

from discord.ext import tasks
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def on_message(self, message):    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if  re.match('^/[1-9]{1}[D]', message.content):
        dice = 1
    else:
        dice = 0
        
    if dice > 0:
        await message.channel.send('Dice')
        i = 0
        count = int(message.content[1:2]) + 1
        dim = int(message.content[3:])
        lst = []
        for i in range(1, count):
            rand_num =  random.randint(1, dim)
            lst.append(rand_num)
        await message.channel.send(lst)
    
    


bot.run(token)
