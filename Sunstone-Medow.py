import timechild
import discord
#from discord_slash import SlashCommand, SlashContext
from discord.ext import commands

bot = commands.Bot()
TOKEN = ""


@bot.slash_command(name="start",description="creates a farm")
async def start(ctx): 
    savefile = open(f"{ctx.author.name}.txt")
    savefile.write()
    print(ctx.author.name)
    await ctx.respond(f"Hey {ctx.author.name} your farm is all ready to go")
    
@bot.slash_command(name="view",description="Shows you your farm and inventory")
async def view(ctx): 
    print(ctx.author)
    await ctx.respond(f"Hey {ctx.author} your farm is all ready to go")    
    
    
    
@bot.slash_command(name="buy",description="buys crop seeds")    
async def buy(ctx, plant_id: int, row: int,colom: str,name="Buy",description="buys the plant with the id given"):
    
  await ctx.respond("done")    

print("Everything is working")
bot.run(TOKEN)