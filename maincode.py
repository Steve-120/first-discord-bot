import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='=')
bot.remove_command("help")


def potatilog_only(func):
	async def wrapper(*args, **kwargs):
		if args[0].guild == bot.get_guild(746364782269038692):
			await func(*args, **kwargs)
	return wrapper

@potatilog_only
async def shame_feet(message):
	uncleaned = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ　ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
	cleaned = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
	cleansor = {}
	for inp, outp in zip(uncleaned, cleaned):
		cleansor[inp] = outp

	cleaned_msg = ''.join([cleansor[x] if x in cleansor else x for x in message.content]).lower()
	cleaned_msg = ''.join(cleaned_msg.split())

	words = ["feet", "foot", "paa", "腳", "脚", "足"]
	for word in words:
		if word in cleaned_msg:
			await message.channel.send('foot fetish sucks')


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
	if message.author.bot: return
	
	await shame_feet(message)
	await bot.process_commands(message)

bot.run(os.environ["DISCORD_TOKEN"])

'''
TODO:

on_message 
if detect "feet/foot": shame foot fetish
'''