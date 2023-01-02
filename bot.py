import subprocess
import discord
from discord.ext import commands
from yeelight import Bulb
import os
bulb = Bulb("192.168.1.6")


intents = discord.Intents().all()
intents.messages = True

bot = commands.Bot(command_prefix="/", intents=intents)
#bot = commands.Bot(command_prefix="/")



#Deneme
@bot.command()
async def merhaba(ctx):
	await ctx.send("Merhaba Dünyalı")


#Işık kontrolleri
@bot.command()
async def nox(ctx):
	await ctx.send("Nox")
	bulb.turn_off()
	
@bot.command()
async def lumos(ctx):
	await ctx.send("Lumos")
	bulb.turn_on()


#Bilgisayar kontrolleri
@bot.command()
async def pcoff(ctx):
	await ctx.send("Bilgisayar Kapatılıyor")
	print(subprocess.run(["/home/pi/pwof.sh",
                "arguments"], shell=False))
@bot.command()
async def pcon(ctx):
	await ctx.send("Bilgisayar Açılıyor")
	print(subprocess.run(["/home/pi/wol.sh",
                "arguments"], shell=False))

#Youtube İndirme Yöneticisi

@bot.command()
async def ytl(ctx, arg1):
	await ctx.send("İndirme Başlatıldı")
	command = 'python3 yt-down.py ' + arg1
	os.system(command)

	


#Anahtar
@bot.event
async def on_ready():
    await bot.get_channel(1006637872331370506).send("Bot geldi HANIMMM")
bot.run("MTA0MDg3Njk5MDU0NDIzNjYzNQ.G-_NTZ.dTKGzadQDs-XSyHXXmlHDZVaRI-NWIUyob6pOY")


