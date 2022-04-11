from discord.ext import commands
from keep_alive import keep_alive
import discord
import os

client = discord.Client()
bot = commands.Bot(command_prefix='!')

guywithsigns = ["|￣￣￣￣￣￣￣￣￣￣￣￣￣|",
       "       we have signs command",
"|＿＿＿＿＿＿＿＿＿＿＿＿＿|",
                    "                   \ (•◡•) /",
                      "                      \      /",
                        "                        ---",
                        "                        |   |"]

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def varoun(ctx, arg):
    token_id = int(arg)
  
    if token_id >= 0 and token_id < 10000:
      base_url = f'https://frames-app-theta.vercel.app/api/p/kiwami/{str(token_id)}'
      await ctx.send(base_url)
    else:
      await ctx.send('Token ID outside of range')

@bot.event
async def on_message(message):
	if message.content == "!varoun signs":
		  await message.channel.send("\n".join(guywithsigns))

	await bot.process_commands(message)


    
keep_alive()
bot.run(os.getenv('TOKEN'))