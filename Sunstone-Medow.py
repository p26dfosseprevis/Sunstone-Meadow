import timechild
import discord
from discord.ext import commands

bot = commands.Bot()
TOKEN = "nice try"


@bot.slash_command(name="ping",description="returns pong")
async def first_slash(ctx): 
    await ctx.respond("Pong")
    
async def buy(ctx, plant_id: int, row: int,colom: str,name="Buy",description="buys the plant with the id given"):
    
  await ctx.respond()    

print("Everything is working")
bot.run(TOKEN)