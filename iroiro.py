import discord
from discord.ext import commands # Bot Commands Frameworkをインポート
import re
import os
import random
from discord.ext import tasks
from datetime import datetime

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # コマンドの作成。コマンドはcommandデコレータで必ず修飾する。
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.Cog.listener()
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
            
    @commands.command()
    async def おみくじ(self, ctx):
            embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの運勢！",
                              color=0x2ECC69)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="[運勢] ", value=random.choice(('姫吉','大吉', '吉' , '中吉' , '小吉' ,'凶', '大凶')), inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=["choose, random"])
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


    @commands.command(filename=None,spoiler=False)
    async def ねこ(self, ctx):
        path = r"C:\Users\watashi\Desktop\騎士君\ねこ"
        files = os.listdir(path)
        neeko = ['にゃあ💛','にゃんっっ! ', 'にゃぁ～？','にゃあにゃあ！', 'にゃ～ん', '猫です。よろしくお願いします。＜〇＞＜〇＞']
        await ctx.send(random.choice(neeko))
        await ctx.send(file=discord.File(path +'/'+random.choice(files)))

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
