import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description="", help_command=None)

@bot.command()
async def help(ctx):
  embed = discord.Embed(
  	title="Help Command | Designing Cosmos", 
  	description="You can use me to find thumbnails, renders and pins for each and every brawler in Brawl Stars! They are totally free-to-use, but do not claim them to be yours. Cool, isn't it?\n\n:white_small_square: Add me in a server! 》[CLICK ME](https://discord.com/api/oauth2/authorize?client_id=837549702635323452&permissions=388160&redirect_uri=https%3A%2F%2Fdiscord.com%2Finvite%2FSA4azVExev&scope=bot)\n\n_These are my commands:_\n```!help                Shows this help panel\n!invite              Add me to your server\n!ping                Shows bot and API latency\n!guilds              Shows the number of servers I'm in\n!<brawler_name>      Obtains free-to-use designs\n!template            Provides common templates\n!font                Provides common designing fonts\n!loadingscreen       Provides different loading screens\n!bg                  Provides different backgrounds\n!text                Provides common Brawl Stars texts```\nIf you have any questions, suggestions, contribution, reports of errors/typos or feedbacks, please DM <@692254240290242601>! For Designing Cosmos server members, you can also DM our <@732537484503810059> bot!! In addition, huge credit and thanks to [Brawl Assets](https://discord.gg/brawlassets) for some of the assets!\n\n__**:warning: Important Notice on <brawler_name>**__\n\n**Please note that the bot is still in the creation status of Beta Version. \nOnly __amber, bibi, belle, bull, buzz, byron, carl, colt, crow, dynamike, edgar, emz, frank, gale, gene, jacky, leon, lou, max, mortis, mr.p, nani, rosa, sandy, spike, sprout, squeak, stu, surge & tick__ designs are available currently.\n\n**Thank you for using our official Designing Cosmos Bot!**", 
  	color=0x000000
  )
  await ctx.send(embed=embed)

# Create Edgar command (i.e. !edgar renders quickdraw)
@bot.command(aliases=["Edgar"])
async def edgar(ctx, content: str): # Define everything after !edgar
    design, skin = content.split(' ') # Split content to design type and skin type respectively
    print(f"Edgar command requested by {ctx.author}") # Log to console
    if design == "renders": # Test if design type is renders
      if skin == "default": # Test if skin is default
        await ctx.send(f"Requested {skin} {ctx} {design}") # Return "Requested default edgar renders"
        print(f"{ctx.author} requested {skin} {ctx} {design}") # Log to console
      elif skin == "quickdraw": # Test is skin is quickdraw
        await ctx.send(f"Requested {skin} {ctx} {design}") # Return "Requested quickdraw edgar renders"
        print(f"{ctx.author} requested {skin} {ctx} {design}") # Log to console
      elif not skin: # If skin is not specified
        await ctx.send("Please specify a skin!") # Return a warning message
        print(f"{ctx.author} requested {ctx} {design} without specifying a skin") # Log to console that "Peter#0001 requested edgar renders without specifying a skin"
      else: # Other unexpected circumstances
        await ctx.send("Sorry! Something went wrong!") # Return error message
        print(f"Something went wrong when {ctx.author} requested {ctx} {design}") # Log to console that "Something went wrong when Peter#0001 requested edgar renders"
    elif design == "thumbnails": # Same as renders, but this time it's thumbnails
      if skin == "default":
        await ctx.send(f"Requested {skin} {ctx} {design}")
        print(f"{ctx.author} requested {skin} {ctx} {design}")
      elif skin == "quickdraw":
        await ctx.send(f"Requested {skin} {ctx} {design}")
        print(f"{ctx.author} requested {skin} {ctx} {design}")
      elif not skin:
        await ctx.send("Please specify a skin!")
        print(f"{ctx.author} requested {ctx} {design} without specifying a skin")
      else:
        await ctx.send("Sorry! Something went wrong!")
        print(f"Something went wrong when {ctx.author} requested {ctx} {design}")
    else: # If design type is neither "renders" or "thumbnails", return an error message
      await ctx.send("Please provide a valid design type!")

# Send an error message when !edgar is sent
@bot.event
async def on_message_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Design Type!")

bot.run('')