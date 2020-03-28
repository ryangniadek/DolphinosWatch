# Discord Bot for Monitoring Dolphinos written in Python
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import LeagueScraper

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='DW!')

@bot.command(name='in')
async def inCommand(ctx):
    response = "@Dolphinos IS PLAYING LEAGUE OF LEGENDS" if LeagueScraper.check_if_ingame else "The neberizer is not playing league. @Dolphinos, time to come online!"
    await ctx.channel.send(response)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     elif not message.content.startswith('DW!'):
#         return
#     elif 'in' in message.content:
#         response = "@Dolphinos IS PLAYING LEAGUE OF LEGENDS" if LeagueScraper.check_if_ingame else "The neberizer is not playing league. @Dolphinos, time to come online!"
#         await message.channel.send(response)
#     elif 'time' in message.content:
#         response = "time in game"
#         await message.channel.send(response)
#     elif 'last' in message.content:
#         response = "last game"
#         await message.channel.send(response)


bot.run(TOKEN)
