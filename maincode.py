import discord
from discord.ext import commands
import os
import random
import github

bot = commands.Bot(command_prefix='=')
bot.remove_command("help")

github_account = github.Github('cc43a95bed740d552b6c52fc42ba636d25eec4c7') # Personal Access Token
data_repo = github_account.get_user().get_repo('first-discord-bot-data')

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

	words = ["feet", "foot", "paa", "腳", "脚", "足", "🦶", "👣"]
	for word in words:
		if word in cleaned_msg:
			await message.channel.send('foot fetish sucks')

@potatilog_only
async def kek_checker(message):
	if message.content.lower() != "kek": return
	kekcount_data = data_repo.get_contents("/kekcounter.txt")
	kekcount = int(kekcount_data.decoded_content.decode())
	kekcount += 1

	await message.channel.send(kekcount)
	data_repo.update_file("kekcounter.txt", '', str(kekcount), kekcount_data.sha)



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
	await kek_checker(message)

	await bot.process_commands(message)

bot.run("NzY2NjI3Mjg1OTg5MzI2ODgx.X4mHTA.suIGunUgh_ppDei6UliZ7jgWOPI")

'''
dont put in commits:

kekcounter.txt
'''