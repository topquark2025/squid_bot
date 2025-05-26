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


@bot.tree.command(name="위치", description="당신의 위치를 추적합니다")
async def 위치(interaction: discord.Interaction):
    await interaction.response.defer()
    location = data.get("location")
    if location:
        lat = location.get("lat")
        lon = location.get("lon")
        await interaction.followup.send(f"위도: {lat}\n경도: {lon}")
    else:
        await interaction.followup.send("위치 정보가 없습니다.")

bot.run(os.getenv("TOKEN"))  # .env 파일의 TOKEN 사용
