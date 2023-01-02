import discord
from discord.ext import commands
import os

from yeelight import Bulb
bulb = Bulb("192.168.1.6")

intents = discord.Intents().all()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

#Işık kontrolleri
@bot.command()
async def lumos(ctx):
	await ctx.send("Lumos")
	bulb.turn_on()

@bot.command()
async def nox(ctx):
	await ctx.send("nox")
	bulb.turn_off()

#Pc kontrolleri
@bot.command()
async def on(ctx):
	await ctx.send("Bilgisayar açıldı")
	os.system('sudo etherwake -i eth0 80:FA:5B:20:7C:1C')

#İndirme Yöneticisi
@bot.command()
async def ytl(ctx, arg1):
	await ctx.send("İndirme Başlatıldı")
	command = 'python3 yt-down.py ' + arg1
	os.system(command)

#Anahtar
@bot.event
async def on_ready():
    await bot.get_channel(1006637872331370506).send("İndirme Modülü Aktif")
bot.run("MTA0MDg3Njk5MDU0NDIzNjYzNQ.G-_NTZ.dTKGzadQDs-XSyHXXmlHDZVaRI-NWIUyob6pOY")
