import discord
import os
import traceback
import re
import os
import math
import random
import asyncio
import set_input
from googletrans import Translator
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime


token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='?')

def Dice(pInputMessage):
    list = []
    string = (re.match('[1-9]{1}[D]', pInputMessage).group())
    dice_amount = string[0]
    dice_faces = pInputMessage[2:]
    for i in range(int(dice_amount)):
        list.append(random.randint(1,int(dice_faces)))
    return list
                
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
#=======================遊び用====================================＝
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
        await ctx.send('結果'+str(Dice(inputmsg)))
        
@bot.command()
async def sayd(ctx, *, message: str):
    """Botに喋らせます（メッセージは自動で削除されます）"""
    await ctx.send(message)
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()
        
@bot.command()
async def kh(ctx, *, message: str):
    #韓国
    msg=translator.translate(message, src='ja' ,dest='ko').text
    await cts.send(msg) 

#================================呼び出し=============================
@bot.command()
async def きりさめ(ctx):
    kirisame = ['きりさめはJKだょ？','きりさめはJCかな？','きりさめはJSヵモ？','きりっっ','きりちゃん☆彡']
    await ctx.send("<@474584379071528960>" + '\n' + random.choice(kirisame))
@bot.command()
async def てんが(ctx):
    await ctx.send('(っ'"'"'-'"'"')╮ =͟͟͞╰U╯ﾌﾞｵﾝ' +"<@487986743266770945>")            

 #====================ROLE付与==========================
ID_CHANNEL_README = set_input.ID_CHANNEL_README # 該当のチャンネルのID  
ID_ROLE_ASA = set_input.ID_ROLE_ASA # 付けたい役職のID  
ID_ROLE_HIRU = set_input.ID_ROLE_HIRU
ID_ROLE_YORU = set_input.ID_ROLE_YORU
ID_ROLE_SINY = set_input.ID_ROLE_SINY
ID_chl_syuti = set_input.ID_chl_syuti
ID_ROLE_SINK = set_input.ID_ROLE_SINK
ID_ROLE_TSKL = set_input.ID_ROLE_TSKL
ID_TSKILL = set_input.ID_TSKILL
@bot.event  
async def on_raw_reaction_add(payload):  
    channel = bot.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        
        if payload.emoji.name == '🌼':
            role = guild.get_role(ID_ROLE_ASA)  
            await member.add_roles(role)  
        
        if payload.emoji.name == '🌞':
            role = guild.get_role(ID_ROLE_HIRU)  
            await member.add_roles(role)  
        
        if payload.emoji.name == '🌝':
            role = guild.get_role(ID_ROLE_YORU)  
            await member.add_roles(role)  
        
        if payload.emoji.name == '🌛':
            role = guild.get_role(ID_ROLE_SINY)  
            await member.add_roles(role)
            
        if payload.emoji.name == '🍌':
            role = guild.get_role(ID_ROLE_SINK)  
            await member.add_roles(role)

    if channel.id == ID_TSKILL:
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        if payload.emoji.name == '🤓':
            role = guild.get_role(ID_ROLE_TSKL)  
            await member.add_roles(role)    
            
@bot.event  
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        
        if payload.emoji.name == '🌼':
            role = guild.get_role(ID_ROLE_ASA)  
            await member.remove_roles(role)  
        
        if payload.emoji.name == '🌞':
            role = guild.get_role(ID_ROLE_HIRU)  
            await member.remove_roles(role)    
        
        if payload.emoji.name == '🌝':
            role = guild.get_role(ID_ROLE_YORU)  
            await member.remove_roles(role)  
        
        if payload.emoji.name == '🌛':
            role = guild.get_role(ID_ROLE_SINY)  
            await member.remove_roles(role)     

        if payload.emoji.name == '🍌':
            role = guild.get_role(ID_ROLE_SINK)  
            await member.remove_roles(role)
            
    if channel.id == ID_TSKILL:   
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        if payload.emoji.name == '🤓':
            role = guild.get_role(ID_ROLE_TSKL)  
            await member.remove_roles(role)
                
#===============================タスキル====

ID_SRV = set_input.ID_SRV
#@tasks.loop(seconds=60)
#async def loop():
#    await bot.wait_until_ready()
#    now  = datetime.now().strftime("%H:%M")
#    if now == '20:00':
#        channel = bot.get_channel(ID_TSKILL)
#        guild = bot.get_guild(ID_SRV)
#        tskl = discord.utils.get(guild.roles,name='タスキル')
#        for member in guild.members:
#            if tskl in member.roles:
#                await member.remove_roles(tskl)
#        poll = await channel.send('今日の凸状況')
#        await poll.add_reaction("1️⃣")
#        await poll.add_reaction("2️⃣")
#        await poll.add_reaction("3️⃣")
      
#        msg = await channel.send('ほんじつのタスキルまん')
#        await msg.add_reaction('🤓')
#loop.start()


#=そのた======================================
@bot.command()
async def コール(ctx, *, message: str):
    """Botに喋らせます（メッセージは自動で削除されます）"""
    msg = await ctx.send(message)
    await msg.add_reaction('🤚')
    await msg.add_reaction('🥺')
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()

@bot.command()
async def 秒数(ctx, zan,la):
    c = 90 - (int(zan) / int(la)) * 90 + 20
    if c > 90:
        c = 90
    if 0 > int(zan) or 0 > int(la):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:        
        await ctx.send(ctx.author.mention + '\n' +  str(math.ceil(c)) + "秒")

@bot.command()
async def フル(ctx, zan):
    f = int(zan) * 4.29
    if 0 > int(zan):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:
        await ctx.send(ctx.author.mention + '\n' +  str(f) + "くらいでフル持越し")

bot.run(token)
