import discord
import os
import traceback
import re
import os
import random
import asyncio
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

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
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
#================================呼び出し=============================
#=ろーる
@bot.command()
async def ぱぱ(ctx):
    await ctx.send("<@&662950715945386016>"+'\nぱぱー！')
@bot.command()
async def くらめん(ctx):
    await ctx.send("<@&549971775828656168>")
@bot.command()
async def あさ(ctx):
    await ctx.send("<@&667737559761158144>")
@bot.command()
async def ひる(ctx):
    await ctx.send("<@&667737624559091712>")
@bot.command()
async def よる(ctx):
    await ctx.send("<@&667737699817488423>")
@bot.command()
async def しんや(ctx):
    await ctx.send("<@&667737720206131200>")
    
#=個人
@bot.command()
async def きりさめ(ctx):
    kirisame = ['きりさめはJKだょ？','きりさめはJCかな？','きりさめはJSヵモ？','きりっっ','きりちゃん☆彡']
    await ctx.send("<@474584379071528960>" + '\n' + random.choice(kirisame))      
@bot.command()
async def てんが(ctx):
    await ctx.send('(っ'"'"'-'"'"')╮ =͟͟͞╰U╯ﾌﾞｵﾝ' +"<@487986743266770945>")            
@bot.command()
async def えくせ(ctx):
    await ctx.send("<@419876101419040776>")
@bot.command()
async def りず(ctx):
    await ctx.send("<@356035126909468675>")        
@bot.command()
async def ぽり(ctx):
    await ctx.send("<@509004043922702347>")
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
    
#====募集=======================================================================================================================

@bot.command()
async def rect(ctx, about = "募集", cnt = 4, settime = 10.0):
    cnt, settime = int(cnt), float(settime)
    reaction_member = [">>>"]
    test = discord.Embed(title=about,colour=0x1e90ff)
    test.add_field(name=f"あと{cnt}人 募集中\n", value=None, inline=True)
    msg = await ctx.send(embed=test)
    #投票の欄
    await msg.add_reaction('⏫')
    await msg.add_reaction('✖')

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji == '⏫' or emoji == '✖'

    while len(reaction_member)-1 <= cnt:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            await ctx.send('人がたりません。')
            break
        else:
            print(str(reaction.emoji))
            if str(reaction.emoji) == '⏫':
                reaction_member.append(user.name)
                cnt -= 1
                test = discord.Embed(title=about,colour=0x1e90ff)
                test.add_field(name=f"あと__{cnt}__人 募集中\n", value='\n'.join(reaction_member), inline=True)
                await msg.edit(embed=test)

                if cnt == 0:
                    test = discord.Embed(title=about,colour=0x1e90ff)
                    test.add_field(name=f"あと__{cnt}__人 募集中\n", value='\n'.join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                    finish = discord.Embed(title=about,colour=0x1e90ff)
                    finish.add_field(name="メンバーがきまりました。",value='\n'.join(reaction_member), inline=True)
                    await ctx.send(embed=finish)

            elif str(reaction.emoji) == '✖':
                if user.name in reaction_member:
                    reaction_member.remove(user.name)
                    cnt += 1
                    test = discord.Embed(title=about,colour=0x1e90ff)
                    test.add_field(name=f"あと__{cnt}__人 募集中\n", value='\n'.join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                else:
                    pass
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)

 #====================ROLE付与==========================

ID_CHANNEL_README = 665211777855913985 # 該当のチャンネルのID  
ID_ROLE_WELCOME = 667699276268306435 # 付けたい役職のID  

@bot.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:  
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)  
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)  
        await channel.send('いらっしゃいませ！')  
    

bot.run(token)    
