import discord
from discord.ext import commands
import os


class varounCommands(commands.Cog):


  def __init__(self, bot):
    self.bot = bot


  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot is online.')


  #Commands
"""
  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong!')
"""




def setup(bot):
  bot.add_cog(varounCommands(bot))