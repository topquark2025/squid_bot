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
