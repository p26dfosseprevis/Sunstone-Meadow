import timechild
import extrafun
import discord
#from discord_slash import SlashCommand, SlashContext
from discord.ext import commands

bot = commands.Bot()
TOKEN = "MTIzMTk3MzM2MzQwNTI5MTUzMA.GTyMmd.fE8QxfEB5BY9i-fWUvGXnxTY46Rio3HTblVRlk"


@bot.slash_command(name="start",description="creates a farm")
async def start(ctx): 
    savefile = open(f"savedata/{ctx.author.name}.txt","w")
    savefile.write("1000\n")
    savefile.write("0\n")
    savefile.write(str([])+"\n")
    savefile.write(str([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])+"\n")
    savefile.write(str([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])+"\n")
    savefile.write(str([["dirt",timechild.today_date()],["dirt",timechild.today_date()],["dirt",timechild.today_date()]])+"\n")
    savefile.close()
    print(ctx.author.name)
    await ctx.respond(f"Hey {ctx.author.name} your farm is all ready to go")
    
@bot.slash_command(name="view",description="Shows you your farm and inventory")
async def view(ctx): 
    savefile = open(f"savedata/{ctx.author.name}.txt","r")
    
    await ctx.respond(f"""You have {extrafun.remove_newline(savefile.readline())} gold
    Your fishing rod is level {extrafun.remove_newline(savefile.readline())}
    Your inventory looks like this {extrafun.remove_newline(savefile.readline())}
    And this is your farm:
    {extrafun.remove_newline(savefile.readline())}
    {extrafun.remove_newline(savefile.readline())}
    {extrafun.remove_newline(savefile.readline())}""")  
    savefile.close()  
    
@bot.slash_command(name="shop",description="Shows the shop")
async def shop(ctx): 
    plants = open("plants.txt","r")
    await ctx.respond(f"""{plants.readlines()}""")
    plants.close()       
    
    
@bot.slash_command(name="buy",description="buys crop seeds")    
async def buy(ctx, plant_id: int, spot_in_farm: str):
    if spot_in_farm != "" OR :
    
    await ctx.respond("done")    




print("Everything is working")
bot.run(TOKEN)