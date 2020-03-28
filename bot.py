# Discord Bot for Monitoring Dolphinos written in Python
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import LeagueScraper as lol

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='DW!')
usernames = ['dolphinos', 'LHemisphere', 'neberizer']

@bot.command(name='in')
async def in_command(ctx):
    in_game = False
    for user in usernames:
        if lol.check_if_ingame(user):
            in_game = True
    response = "@Dolphinos IS PLAYING LEAGUE OF LEGENDS" if in_game else "The neberizer is not playing league. @Dolphinos, time to come online!"
    await ctx.send(response)

@bot.command(name='time')
async def time_command(ctx):
    for user in usernames:
        if lol.check_if_ingame(user):
            await ctx.send("%s has been in game for %d seconds" % (user, lol.get_match_time(user)))
            return
    await ctx.send("The bbern is not in a game")

@bot.command(name='last')
async def last_command(ctx):
    response = "last game"
    await ctx.send(response)

bot.run(TOKEN)
