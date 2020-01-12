import discord
import os
import traceback
import re
import os
import random
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']

def Dice(pInputMessage):
    list = []
    string = (re.match('[1-9]{1}[D]', pInputMessage).group())
    dice_amount = string[0]
    dice_faces = pInputMessage[2:]
    
    for i in range(int(dice_amount)):
        list.append(random.randint(1,int(dice_faces)))

    return list

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def おみくじ(ctx):
    embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの運勢！",color=0x2ECC69)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="[運勢] ", value=random.choice(('姫吉','大吉', '吉' , '中吉' , '小吉' ,'凶', '大凶')), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ちょいす(ctx, *choices):
    """ここけすな"""
    if choices:
        await ctx.send(random.choice(choices))
    else:
        await ctx.show_help()

@bot.command()
async def だいす(ctx, inputmsg):
    if  re.match('[1-9]{1}[D]', inputmsg):
        dice = 1
    else:
        dice = 0
        
    if dice == 1:
        await ctx.send(Dice(inputmsg))
    
@bot.command()
async def きりさめ(ctx):
    kirisame = ['きりさめはJKだょ？','きりさめはJCかな？','きりさめはJSヵモ？','きりっっ','きりちゃん☆彡']
    await ctx.send("<@474584379071528960>" + '\n' + random.choice(kirisame))      

@bot.command()
async def TENGA(ctx):
    await ctx.send('(っ'"'"'-'"'"')╮ =͟͟͞╰U╯ﾌﾞｵﾝ' +"<@487986743266770945>")            

@bot.command()
async def ぱぱ(ctx):
    await ctx.send("<@&662950715945386016>"+'\nぱぱー！')

@bot.command()
async def くらめん(ctx):
    await ctx.send("<@&549971775828656168>")

@bot.command()
async def えくせ(ctx):
    await ctx.send("<@419876101419040776>")

@bot.command()
async def りず(ctx):
    await ctx.send("<@356035126909468675>")        

@bot.command()
async def おいぬ(ctx):
    await ctx.send("<@224042826520854528>")
    
@bot.command(filename=None,spoiler=False)
async def ねこ(ctx):
    #path = r"C:\Users\watashi\Desktop\騎士君\ねこ"
    #files = os.listdir(path)
    neeko = ['にゃあ💛','にゃんっっ! ', 'にゃぁ～？','にゃあにゃあ！', 'にゃ～ん', '猫です。よろしくお願いします。＜〇＞＜〇＞']
    await ctx.send(random.choice(neeko))
    #await ctx.send(file=discord.File(path +'/'+random.choice(files)))

bot.run(token)
