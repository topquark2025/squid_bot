from server import run_forever #서버

import discord
from discord.ext import commands , tasks
from discord.ui import View, Select
from discord import app_commands

from dotenv import load_dotenv

import aiohttp
import asyncio
from selectolax.parser import HTMLParser
import os
load_dotenv()  # .env 파일에서 TOKEN 등 불러오기
run_forever()   # 플라스크 서버 실행 (Render 유지용)





color = discord.Color.blue()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

    print(f'봇 로그인됨: {bot.user}')
    await bot.change_presence(status=discord.Status.idle)