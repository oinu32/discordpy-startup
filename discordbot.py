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

@bot.command(aliases=["choose, random"])
    async def ちょいす(self, ctx, *choices):
        """ここけすな"""
        if choices:
            await ctx.send(random.choice(choices))
        else:
            await ctx.show_help()
@commands.command()
async def きりさめ(self, ctx):
    kirisame = ['きりさめはJKだょ？','きりさめはJCだょ！','きりさめはJSかも？','きりっっ','きりちゃん☆彡','キリンリキ']
    await ctx.send("<@474584379071528960>" + '\n' + random.choice(kirisame))      
@commands.command()
async def TENGA(self, ctx):
    await ctx.send('(っ'"'"'-'"'"')╮ =͟͟͞╰U╯ﾌﾞｵﾝ' +"<@487986743266770945>")            
@commands.command()
async def ぱぱ(self, ctx):
    await ctx.send("<@&662950715945386016>"+'\nぱぱー！')
@commands.command()
async def くらめん(self, ctx):
    await ctx.send("<@&549971775828656168>")
@commands.command()
async def えくせ(self, ctx):
    await ctx.send("<@419876101419040776>")
@commands.command()
async def りず(self, ctx):
    await ctx.send("<@356035126909468675>")


    


bot.run(token)
