import discord
from discord.ext import commands

print("hi")
bot = commands.Bot(command_prefix='?')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.event
async def on_ready():
    print('Ready!')

    
bot.run()