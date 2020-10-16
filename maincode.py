import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='=')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def lenny(ctx):
	await ctx.send('( ͡° ͜ʖ ͡°)')

@bot.command()
async def silog(ctx):
	silog_list = ['Tapsilog', 'Longsilog', 'Tocilog', 'Bangsilog', 'Cornsilog', 'Hotsilog', 'Porksilog', 'Chicksilog', 'Sisigsilog']
	await ctx.send(random.choice(silog_list))

bot.run(os.environ['DISCORD_TOKEN'])