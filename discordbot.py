import discord
import os
import traceback
import re
import os
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

#翻訳群      
@bot.command()
async def kh(ctx, *, message):
    """ ja →　ko """
    #韓国
    translator = Translator()  
    msg=translator.translate(ctx.message.clean_content[4:] , src='ja' ,dest='ko')
    await ctx.send(msg.text) 

@bot.command()
async def jh(ctx, *, message):
    """ko　→ ja"""
    translator = Translator()
    msg=translator.translate(ctx.message.clean_content[4:], src='ko' ,dest='ja')
    await ctx.send(msg.text) 
    
@bot.command()
async def jeh(ctx, *, message):
    """ja　→en"""
    #英語
    translator = Translator()  
    msg=translator.translate(ctx.message.clean_content[4:] , src='ja' ,dest='en')
    await ctx.send(msg.text) 

@bot.command()
async def ejh(ctx, *, message):
    """en→ja"""
    #english→日本
    translator = Translator()  
    msg=translator.translate(ctx.message.clean_content[4:], src='en' ,dest='ja')
    await ctx.send(msg.text) 
    
@bot.command()
async def jch(ctx, *, message):
    """ja→zh-CN"""
    #中国語
    translator = Translator()  
    msg=translator.translate(ctx.message.clean_content[4:] , src='ja' ,dest='zh-CN')
    await ctx.send(msg.text) 

@bot.command()
async def cjh(ctx, *, message):
    """zh-CN→ja"""
    #ちゃいにーず→日本
    translator = Translator()  
    msg=translator.translate(ctx.message.clean_content[4:], src='zh-CN' ,dest='ja')
    await ctx.send(msg.text)

    
#================================呼び出し=============================
@bot.command()
async def きりさめ(ctx):
    """きりさめを呼ぶ"""
    kirisame = ['きりさめはJKだょ？','きりさめはJCかな？','きりさめはJSヵモ？','きりっっ','きりちゃん☆彡']
    await ctx.send("<@474584379071528960>" + '\n' + random.choice(kirisame))
#@bot.command()
#async def てんが(ctx):
#    await ctx.send('(っ'"'"'-'"'"')╮ =͟͟͞╰U╯ﾌﾞｵﾝ' +"<@487986743266770945>")            

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
ID_TSKILL2 = set_input.ID_TSKILL2
ID_totu = set_input.ID_totu
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

    if channel.id == ID_TSKILL or channel.id == ID_TSKILL2:
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
            
    if channel.id == ID_TSKILL or channel.id == ID_TSKILL2:   
        guild = bot.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id) 
        if payload.emoji.name == '🤓':
            role = guild.get_role(ID_ROLE_TSKL)  
            await member.remove_roles(role)
                
#===============================タスキル====
emoji1 = '<:cnt1:739818340939202622>'
emoji2 = '<:cnt2:739818340557783063>'
emoji3 = '<:cnt3:739818340918493273>'
emoji4 = '<:cnt4:739818340788207617>'
emoji5 = '<:cnt5:739818340905648208>'
ID_SRV = set_input.ID_SRV

@tasks.loop(seconds=60)
async def loop():
    await bot.wait_until_ready()
    now  = datetime.now().strftime("%H:%M")
    if now == '20:00':
        channel = bot.get_channel(ID_TSKILL)
        channel2 = bot.get_channel(ID_TSKILL2)
        channel3 = bot.get_channel(ID_totu)
        guild = bot.get_guild(ID_SRV)
        tskl = discord.utils.get(guild.roles,name='タスキル')

        for member in guild.members:
            if tskl in member.roles:
                await member.remove_roles(tskl)
        poll = await channel.send('今日の凸状況')
        await poll.add_reaction("1️⃣")
        await poll.add_reaction("2️⃣")
        await poll.add_reaction("3️⃣")
        msg = await channel.send('本日のKIMURA Chance')
        await msg.add_reaction('🤓')

        msg = await channel3.send("今日の凸予定先" + '\n' + "1️⃣～5️⃣：物理" + '\n' + '<:cnt1:739818340939202622>' + "～" + '<:cnt5:739818340905648208>' + "：魔法")
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction(emoji1)
        await msg.add_reaction(emoji2)
        await msg.add_reaction(emoji3)
        await msg.add_reaction(emoji4)
        await msg.add_reaction(emoji5)
         
        msg2 = await channel2.send('本日のKIMURA Chance')
        await msg2.add_reaction('🤓')
        
        msg3 = await channel3.send("今日の凸予定先" + '\n' + "1️⃣～5️⃣：物理" + '\n' + '<:cnt1:739818340939202622>' + "～" + '<:cnt5:739818340905648208>' + "：魔法")
        await msg3.add_reaction("1️⃣")
        await msg3.add_reaction("2️⃣")
        await msg3.add_reaction("3️⃣")
        await msg3.add_reaction("4️⃣")
        await msg3.add_reaction("5️⃣")
        await msg3.add_reaction(emoji1)
        await msg3.add_reaction(emoji2)
        await msg3.add_reaction(emoji3)
        await msg3.add_reaction(emoji4)
        await msg3.add_reaction(emoji5)
        
loop.start()

#=そのた======================================
@bot.command()
async def コール(ctx, *, message: str):
    """🤚は凸、🥺は持ち越し吐きたい人"""
    msg = await ctx.send(message)
    await msg.add_reaction('🤚')
    await msg.add_reaction('🥺')
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()

@bot.command()
async def 凸(ctx):
    """私はここに凸したいってところにリアクションつけようね"""
    msg = await ctx.send("今日の凸予定先" + '\n' + "1️⃣～5️⃣：物理" + '\n' + '<:cnt1:739818340939202622>' + "～" + '<:cnt5:739818340905648208>' + "：魔法")
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")
    await msg.add_reaction("5️⃣")
    await msg.add_reaction(emoji1)
    await msg.add_reaction(emoji2)
    await msg.add_reaction(emoji3)
    await msg.add_reaction(emoji4)
    await msg.add_reaction(emoji5)
    # message can't be deleted in private channel(DM/Group)
    if not isinstance(ctx.message.channel, discord.abc.PrivateChannel):
        await ctx.message.delete()
        
useflag = False
@bot.event
async def on_message(message):
    
    if message.author.bot:
        return
    
    def check(msg):
        return True
    #msg.author == message.author
    
#    if useflag:
#        return
    
    if message.content.startswith("/count"):
#        useflag = True
        await message.channel.send("以下からカウントします。")
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
            dmgMatch = re.match(r'[0-9]+万', string) 
            
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
#        useflag=False
    
    await bot.process_commands(message)   
        
        
        
@bot.command()
async def 秒数(ctx, zan,la):
    """?秒数　残HP LAの人のダメージ　持越し秒数"""
    c = 90 - (int(zan) / int(la)) * 90 + 20
    if c > 90:
        c = 90
    if 0 > int(zan) or 0 > int(la):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:        
        await ctx.send(ctx.author.mention + '\n' +  str(math.ceil(c)) + "秒")

@bot.command()
async def フル(ctx, zan):
    """?フル　残HP　どのぐらい出せばフル持越しになるか"""
    f = int(zan) * 4.29
    if 0 > int(zan):
        await ctx.send(ctx.author.mention + '\n' + "正しい数値を入力してください")
    else:
        await ctx.send(ctx.author.mention + '\n' +  str(f) + "くらいでフル持越し")

        
bot.run(token)
