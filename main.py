from discord.ext import commands
from keep_alive import keep_alive
import discord
import os

client = discord.Client()
bot = commands.Bot(command_prefix='!varoun')

def is_int(num):
  try:
    int(num)
    return True
  except:
    return False

guywithsigns = ["|￣￣￣￣￣￣￣￣￣￣￣￣￣|",
       "       we have signs command",
"|＿＿＿＿＿＿＿＿＿＿＿＿＿|",
                    "                   \ (•◡•) /",
                      "                      \      /",
                        "                        ---",
                        "                        |   |"]

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    msg_parts = msg.split(' ')

#Code for masked kiwami images
    if msg_parts[0] == '!varoun':
      if is_int(msg_parts[1]):
        token_id = int(msg_parts[1])
        # number validation
        if token_id >= 0 and token_id < 10000:
          base_url_normal = f'https://frames-nft-app.herokuapp.com/api/os/0x701A038aF4Bd0fc9b69A829DdcB2f61185a49568/{str(token_id)}'
          await message.channel.send(base_url_normal)
        else:
          await message.channel.send('Token ID outside of range')
#Code for normal kiwami images
      elif msg_parts[1] == 'logo':
        if is_int(msg_parts[2]):
          token_id = int(msg_parts[2])
          if token_id >= 0 and token_id < 10000:
            base_url_logo = f'https://frames-app-theta.vercel.app/api/p/kiwami/{str(token_id)}'
            await message.channel.send(base_url_logo)
          else:
            await message.channel.send('Token ID outside of range')
#Code for sign board
      elif msg_parts[1] == 'signs':
        await message.channel.send("\n".join(guywithsigns))


    
keep_alive()
bot.run(os.getenv('TOKEN'))