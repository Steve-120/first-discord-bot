import discord
from discord.ext import commands
import os 

bot = commands.Bot(command_prefix='=')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def lenny(ctx):
	await ctx.send('( ͡° ͜ʖ ͡°)')

bot.run(os.environ['DISCORD_TOKEN'])