import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='=')
bot.remove_command("help")

@bot.command()
async def ping(ctx):
	await ctx.send("pong")

@bot.command()
async def lenny(ctx):
	await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def silog(ctx):
	silog_list = ["Tapsilog", "Longsilog", "Tocilog", "Bangsilog", "Cornsilog", "Hotsilog", "Porksilog", "Chicksilog", "Sisigsilog"]
	await ctx.send(random.choice(silog_list))

@bot.event
async def on_ready():

	discord_status = discord.Activity(type = discord.ActivityType.watching, name = "if you be anti-PRC")
	await bot.change_presence(activity = discord_status)

bot.run(os.environ["DISCORD_TOKEN"])