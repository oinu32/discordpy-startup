import discord
import os
import traceback
import re
import math
import random
import asyncio
import set_input

import MessageController
import DamageCalculator

from googletrans import Translator

from discord.ext import tasks
from discord.ext import commands
from datetime import datetime

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)
    
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
    """?おみくじ　おみくじひける"""
    embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの運勢！",color=0x2ECC69)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="[運勢] ", value=random.choice(('姫吉','大吉', '吉' , '中吉' , '小吉' ,'凶', '大凶')), inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def ちょいす(ctx, *choices):
    """?ちょいす a b c ...ってやるとどれか一つ選んでくれる"""
    if choices:
        await ctx.send(random.choice(choices))
    else:
        await ctx.show_help()
@bot.command()
async def だいす(ctx, inputmsg):
    """?ダイス　nDN でだいすふれるよ"""
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
ID_totu2 = set_input.ID_totu2

chlist = [ID_TSKILL, ID_totu2]
@bot.event  
async def on_raw_reaction_add(payload): 
    guild = bot.get_guild(payload.guild_id) 
    channel = bot.get_channel(payload.channel_id)  
    ch_name = discord.utils.get(guild.text_channels, name="凸管理")
 
    member = guild.get_member(payload.user_id)
    
    tskl = discord.utils.get(guild.roles,name='タスキル')
    ID_1t = discord.utils.get(guild.roles,name='1凸')
    ID_2t = discord.utils.get(guild.roles,name='2凸')
    ID_3t = discord.utils.get(guild.roles,name='3凸')
    
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
    
    if channel.id == ch_name:
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        if payload.emoji.name == '🤓':
            await member.add_roles(tskl)         
        if payload.emoji.name == '1️⃣': 
            await member.add_roles(ID_1t)   
        if payload.emoji.name == '2️⃣':
            await member.add_roles(ID_2t)  
            await member.remove_roles(ID_1t)  
        if payload.emoji.name == '3️⃣':
            await member.remove_roles(ID_1t)
            await member.remove_roles(ID_2t)  
            await member.add_roles(ID_3t)  
    await ctx.send(channel)
    await ctx.send(ch_name)   

@bot.event  
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(payload.channel_id) 
    tskl = discord.utils.get(guild.roles,name='タスキル')
    ID_1t = discord.utils.get(guild.roles,name='1凸')
    ID_2t = discord.utils.get(guild.roles,name='2凸')
    ID_3t = discord.utils.get(guild.roles,name='3凸')
    member = guild.get_member(payload.user_id)
    
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
            
    for chname in chlist:       
        if channel.id == chname:
            guild = bot.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id) 
            if payload.emoji.name == '🤓':
                await member.remove_roles(tskl) 
            if payload.emoji.name == '1️⃣':
                await member.remove_roles(ID_1t)      
            if payload.emoji.name == '2️⃣':
                await member.remove_roles(ID_2t)  
            if payload.emoji.name == '3️⃣':
                await member.remove_roles(ID_3t)
                
            
#===============================タスキル====
emoji1 = '<:cnt1:739818340939202622>'
emoji2 = '<:cnt2:739818340557783063>'
emoji3 = '<:cnt3:739818340918493273>'
emoji4 = '<:cnt4:739818340788207617>'
emoji5 = '<:cnt5:739818340905648208>'

yt1 = '<:yt1:760140566263889931>'
yt2 = '<:yt2:760141171347161178>'
yt3 = '<:yt3:760141171405226024>'
yt4 = '<:yt4:760141224300118036>'
yt5 = '<:yt5:760141238736519169>'

ID_SRV = set_input.ID_SRV
@tasks.loop(seconds=60)
async def loop():
    await bot.wait_until_ready()
    now  = datetime.now().strftime("%H:%M")
    if now == '20:00':
        guild = bot.get_guild(ID_SRV)
        ch_name = discord.utils.get(guild.text_channels, name="凸管理")
        tskl = discord.utils.get(guild.roles,name='タスキル')
        ID_1t = discord.utils.get(guild.roles,name='1凸')
        ID_2t = discord.utils.get(guild.roles,name='2凸')
        ID_3t = discord.utils.get(guild.roles,name='3凸')
        for member in guild.members:
            if tskl in member.roles:
                await member.remove_roles(tskl)
            if ID_1t in member.roles:
                await member.remove_roles(ID_1t)
            if ID_2t in member.roles:
                await member.remove_roles(ID_2t)
            if ID_3t in member.roles:
                await member.remove_roles(ID_3t) 
                

        channel = bot.get_channel(ch_name)            
        poll = await channel.send('今日の凸状況')
        await poll.add_reaction("1️⃣")
        await poll.add_reaction("2️⃣")
        await poll.add_reaction("3️⃣")
        msg2 = await channel.send('本日のKIMURA Chance')
        await msg2.add_reaction('🤓')
        
        msg3 = await channel.send("今日の凸予定先" + '\n' + "1️⃣～5️⃣：物理" + '\n' + '<:cnt1:739818340939202622>' + "～" + '<:cnt5:739818340905648208>' + "：魔法")
        await msg3.add_reaction(yt1)
        await msg3.add_reaction(yt2)
        await msg3.add_reaction(yt3)
        await msg3.add_reaction(yt4)
        await msg3.add_reaction(yt5)
        await msg3.add_reaction(emoji1)
        await msg3.add_reaction(emoji2)
        await msg3.add_reaction(emoji3)
        await msg3.add_reaction(emoji4)
        await msg3.add_reaction(emoji5)        
    
loop.start()

#=そのた======================================
@bot.command()
async def コール(ctx, *, message: str):
    """?コール　"文章"（※必須、「１ボス」とか）　　🤚は凸、🥺は持ち越し吐きたい人"""
    msg = await ctx.send(message)
    await msg.add_reaction('🤚')
    await msg.add_reaction('🥺')
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()
        
@bot.command()
async def call2(ctx, *, message: str):
    """?call2　"文章"（※必須、「１ボス」とか）　　🤚は凸、🥺は持ち越し吐きたい人🤣はフルオート"""
    msg = await ctx.send(message)
    await msg.add_reaction('🤚')
    await msg.add_reaction('🤣')
    await msg.add_reaction('🥺')
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()
        
@bot.command()
async def call(ctx):
    msg = await ctx.send("1boss\n物理1️⃣\n魔法<:cnt1:739818340939202622>\n持越し🥺")
    await msg.add_reaction("1️⃣")
    await msg.add_reaction(emoji1)
    await msg.add_reaction('🥺')
    
    msg2 = await ctx.send("2boss\n物理2⃣\n魔法<:cnt2:739818340557783063>\n持越し🥺")
    await msg2.add_reaction("2️⃣")
    await msg2.add_reaction(emoji2)
    await msg2.add_reaction('🥺')
    
    msg3 = await ctx.send("3boss\n物理3⃣\n魔法<:cnt3:739818340918493273>\n持越し🥺")
    await msg3.add_reaction("3️⃣")
    await msg3.add_reaction(emoji3)
    await msg3.add_reaction('🥺')
    
    msg4 = await ctx.send("4boss\n物理4⃣\n魔法<:cnt4:739818340788207617>\n持越し🥺")
    await msg4.add_reaction("4️⃣")
    await msg4.add_reaction(emoji4)
    await msg4.add_reaction('🥺')
    
    msg5 = await ctx.send("5boss\n物理5⃣\n魔法<:cnt5:739818340905648208>\n持越し🥺")
    await msg5.add_reaction("5️⃣")
    await msg5.add_reaction(emoji5)
    await msg5.add_reaction('🥺')
    
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()
        

@bot.command()
async def 秒数(ctx, zan,la):
    """?秒数　残HP LAの人のダメージ　＝持越し秒数がでる(90秒まるまる殴った場合のやつなのでズレ有)"""
    c = 90 - (int(zan) / int(la)) * 90 + 20
    if c > 90:
        c = 90
    if 0 > int(zan) or 0 > int(la):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:        
        await ctx.send(ctx.author.mention + '\n' +  str(math.ceil(c)) + "秒")

@bot.command()
async def 秒数2(ctx, byo,zan,la):
    """?秒数　戦闘時間　残HP LAの人のダメージ　＝持越し秒数がでる　（正確なほう）"""
    c = 110 - int(byo) * (int(zan) / int(la))
    await ctx.send(ctx.author.mention + '\n' +  str(math.ceil(c)) + "秒")

@bot.command()
async def 秒数3(ctx, zan,la,la2):
    """?秒数　戦闘時間　残HP ひとりめ　ふたりめ　＝持越し秒数がでる　フルタイム前提"""
    b = int(zan) - int(la2)
    c = 90 - (int(b) / int(la)) * 90 + 20
    if c > 90:
        c = 90  
    b2 = int(zan) - int(la)
    c2 = 90 - (int(b2) / int(la2)) * 90 + 20
    if c2 > 90:
        c2 = 90  
    await ctx.send(ctx.author.mention + '\nひとりめが後の場合\n' +  str(math.ceil(c)) + '秒\nふたりめが後の場合\n' +  str(math.ceil(c2)) + "秒")

@bot.command()
async def フル(ctx, zan):
    """?フル　残HP　どのぐらい出せばフル持越しになるか"""
    f = int(zan) * 4.29
    if 0 > int(zan):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:
        await ctx.send(ctx.author.mention + '\n' +  str(f) + "くらいでフル持越し")        

        
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    def check(msg):
        return True   
    
    if message.content.startswith("/count"):
        await message.channel.send("以下からカウントします。\n ダメージに　まん　をつけて報告お願いします。")
        DmgCalc = DamageCalculator.DamageCalculator()
        isEnd = False                   
        while (not isEnd):
            wait_msg = await bot.wait_for("message", check=check)
            string = wait_msg.content
            #終了の処理
            if (string == "/end"):
                print("カウントを終了します")
                isEnd = True
                continue
                
            #結果を抽出する
            #dmgMatch = re.match(r'[0-9]+万', string) 
            dmgMatch = re.search(r'[0-9]+まん', string) 
            
            if(dmgMatch == None):
                print("無効なダメージ入力です")
                continue
                
            #以下は有効な入力
            dmg10e4 = re.match(r'[0-9]+', dmgMatch.group())#100万->100にする
            print(dmg10e4.group() + "(万)をデータに追加しました")#debug用
            
            DmgCalc.InsertResult(str(wait_msg.author.name), int(dmg10e4.group()))#ダメージ計算機に結果を追加 
            
        DmgCalc.CalcResult()#合計を計算        
        dmg_msg = str()          
        for resultTaple in DmgCalc.GetResult():
            dmg_msg = dmg_msg + str("名前:" + resultTaple[0] + " " + "スコア:" + str(resultTaple[1]) + "万") + '\n'        
        dmg_msg = dmg_msg + str("合計" + str(DmgCalc.GetResultTotal()) + "万")        
        await message.channel.send(dmg_msg)    
    await bot.process_commands(message)   
    
    if message.content.startswith("/wcount"):
        await message.channel.send("以下からカウントします。\n ダメージに　ちん　をつけて報告お願いします。")
        DmgCalc2 = DamageCalculator.DamageCalculator()
        isEnd = False                   
        while (not isEnd):
            wait_msg = await bot.wait_for("message", check=check)
            string = wait_msg.content
            #終了の処理
            if (string == "/endw"):
                print("カウントを終了します")
                isEnd = True
                continue
                
            #結果を抽出する
            #dmgMatch = re.match(r'[0-9]+万', string) 
            dmgMatch2 = re.search(r'[0-9]+ちん', string) 
            
            if(dmgMatch2 == None):
                print("無効なダメージ入力です")
                continue
                
            #以下は有効な入力
            dmg10e5 = re.match(r'[0-9]+', dmgMatch2.group())#100万->100にする
            print(dmg10e5.group() + "(万)をデータに追加しました")#debug用
            
            DmgCalc2.InsertResult(str(wait_msg.author.name), int(dmg10e5.group()))#ダメージ計算機に結果を追加 
            
        DmgCalc2.CalcResult()#合計を計算        
        dmg_msg = str()          
        for resultTaple in DmgCalc2.GetResult():
            dmg_msg = dmg_msg + str("名前:" + resultTaple[0] + " " + "スコア:" + str(resultTaple[1]) + "万") + '\n'        
        dmg_msg = dmg_msg + str("合計" + str(DmgCalc2.GetResultTotal()) + "万")        
        await message.channel.send(dmg_msg)    
        await bot.process_commands(message)   
        

bot.run(token)
