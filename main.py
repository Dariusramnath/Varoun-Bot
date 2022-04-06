from discord.ext import commands
from keep_alive import keep_alive
import discord
import os

client = discord.Client()
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user} has arrived!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    msg_parts = msg.split(' ')

    if msg_parts[0] == '!varoun':
        # number validation
        try:
            token_id = int(msg_parts[1])
        except:
            await message.channel.send('Invalid Token ID')

        if token_id >= 0 and token_id < 10000:
            base_url = f'https://frames-app-theta.vercel.app/api/p/kiwami/{str(token_id)}'
            await message.channel.send(base_url)
        else:
            await message.channel.send('Token ID outside of range')


keep_alive()
bot.run(os.getenv('TOKEN'))