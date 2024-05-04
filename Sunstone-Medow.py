import timechild
import extrafun
import ast
from discord.ext import commands

bot = commands.Bot()

spots_farm = {"a1":4,"a2":5,"a3":6,"b1":7,"b2":8,"b3":9,"b4":10,"b5":11,"b6":12,}
crop_sell = {"dirt":0,"carrot":50,"potato":400,"parsnip":150,"corn":800}
crop_emo={"dirt":0,"carrot":50,"potato":400,"parsnip":150,"corn":0}
@bot.slash_command(name="start",description="creates a farm")
async def start(ctx): 
    savefile = open(f"savedata/{ctx.author.name}.txt","w")
    savefile.write("1000\n")
    savefile.write("0\n")
    savefile.write(str([])+"\n")
    for i in range(0,9):
        savefile.write(str(["dirt",timechild.today_date()])+"\n")
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
    {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())}
    {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())}
    {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())} {extrafun.remove_newline(savefile.readline())}""")  
    savefile.close()  
    
@bot.slash_command(name="shop",description="Shows the shop")
async def shop(ctx): 
    with open("plants.txt", 'r') as file:
        lines = file.readlines()
        lines_with_numbers = [(i+1, line.strip()) for i, line in enumerate(lines)]
        lines_string = '\n'.join([f"{num}: {content}" for num, content in lines_with_numbers])
        await ctx.respond(lines_string)   
    
    
@bot.slash_command(name="buy",description="buys crop seeds")    
async def buy(ctx, plant_id: int, spot_in_farm: str):
    savedata = f"savedata/{ctx.author.name}.txt"
    if spot_in_farm not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3",] :
        await ctx.respond("thats not a valid location on the farm \n try something like a1 or b3")
        
    elif int(extrafun.get_line_in_file(savedata,1)) < int((extrafun.get_line_in_file("plants.txt",plant_id))[1]):
        await ctx.respond("you don't have enuf money to buy that")
        
    else:
        new_crop_def = extrafun.get_line_in_file("plants.txt",plant_id)  
        new_crop = [new_crop_def[0],timechild.add_times(timechild.today_date(),new_crop_def[3])]
        extrafun.overwrite_line(savedata,spots_farm[spot_in_farm],new_crop)
        extrafun.overwrite_line(savedata,1,int(extrafun.get_line_in_file(savedata,1)) - int((extrafun.get_line_in_file("plants.txt",plant_id))[1]))
        await ctx.respond(f"done bought a {new_crop_def[0]} and planted it on tile {spot_in_farm} for {new_crop_def[1]} \nyou now have {extrafun.get_line_in_file(savedata,1)} gold")   


@bot.slash_command(name="sell",description="sells a crop in your farm")    
async def buy(ctx, spot_in_farm: str):
    savedata = f"savedata/{ctx.author.name}.txt"
    if spot_in_farm not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3",] :
        await ctx.respond("thats not a valid location on the farm \n try something like a1 or b3")
    else:
        crop_data = (extrafun.get_line_in_file(savedata,spots_farm[spot_in_farm]))
        if timechild.is_larger(timechild.today_date(),crop_data[1]):
            extrafun.overwrite_line(savedata,spots_farm[spot_in_farm],str(["dirt",timechild.today_date()]))
            extrafun.overwrite_line(savedata,1,int(extrafun.get_line_in_file(savedata,1)) + crop_sell[str(crop_data[0])])
            await ctx.respond(f"you sold a {crop_data[0]} for {crop_sell[str(crop_data[0])]} gold")
        else:
            await ctx.respond("sorry thats not done growing yet")

fish = [["Name","price","pun"],]
@bot.slash_command(name="fish",description="so why does every game have fishing in it? oh they make it a law a few years ago. im honestly impressed how they cramed it into turbo crash")    
async def buy(ctx):
    savedata = f"savedata/{ctx.author.name}.txt"
    extrafun.overwrite_line(savedata,1,int(extrafun.get_line_in_file(savedata,1)) + 0)

print("Everything is working")
bot.run(TOKEN)