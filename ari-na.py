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
bot = commands.Bot(command_prefix='?ari')
