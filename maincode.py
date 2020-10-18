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

@bot.event
async def on_message(message):
	shame_feet(message)

bot.run(os.environ["DISCORD_TOKEN"])


def potatilog_only(func):
	async def wrapper(*args, **kwargs):
		if args[0].guild == bot.get_guild(698910736117923951):
			func(*args, **kwargs)
	return wrapper

@potatilog_only()
async def shame_feet(message):
	uncleaned = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ　ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
	cleaned = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
	cleansor = {}
	for inp, outp in zip(uncleaned, cleaned):
		filterer[inp] = outp

	cleaned_msg = ''.join([cleansor[x] if x in cleansor else x for x in ctx.message.content]).lower()

	if 'feet' in cleaned_msg:
		await message.channel.send('feet fetish sucks')
'''
TODO:

on_message 
if detect "feet/foot": shame foot fetish
'''