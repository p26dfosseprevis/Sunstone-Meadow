import discord
from discord.ext import commands

bot = commands.Bot()
TOKEN = "nice try"


@bot.slash_command(name="ping",description="returns pong")
async def first_slash(ctx): 
    await ctx.respond("Pong")

print("Everything is working")
bot.run(TOKEN)