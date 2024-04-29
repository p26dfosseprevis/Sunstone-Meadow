import timechild
import discord
#from discord_slash import SlashCommand, SlashContext
from discord.ext import commands

bot = commands.Bot()
TOKEN = ""


@bot.slash_command(name="start",description="creates a farm")
async def start(ctx): 
    savefile = open(f"savedata/{ctx.author.name}.txt","w")
    savefile.write("1000")
    savefile.write("0")
    savefile.write([])
    savefile.write([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])
    savefile.write([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])
    savefile.write([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])
    savefile.close()
    print(ctx.author.name)
    await ctx.respond(f"Hey {ctx.author.name} your farm is all ready to go")
    
@bot.slash_command(name="view",description="Shows you your farm and inventory")
async def view(ctx): 
    savefile = open(f"savedata/{ctx.author.name}.txt","r")
    
    await ctx.respond(f"""You have {savefile.readline()} gold
    Your fishing rod is level {savefile.readline()}
    Your inventory looks like this {savefile.readline()}
    And this is your farm:
    {savefile.readline()}
    {savefile.readline()}
    {savefile.readline()}""")  
    savefile.close()  
    
@bot.slash_command(name="shop",description="Shows the shop")
async def shop(ctx): 

    await ctx.respond(f"Hey {ctx.author} your farm is all ready to go")       
    
    
@bot.slash_command(name="buy",description="buys crop seeds")    
async def buy(ctx, plant_id: int, row: int,colom: str):
    
  await ctx.respond("done")    

print("Everything is working")
bot.run(TOKEN)