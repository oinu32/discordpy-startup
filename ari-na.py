import discord
import os
import traceback
import re
import math
import random
import asyncio
import set_input
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='?ari')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')



bot.run(token)
