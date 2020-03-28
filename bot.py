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
helper = {
    'in': 'Checks if dolphinos is in a game on any of his accounts. Pass an optional paramter to check for another user.',
    'time': 'Checks how long dolphinos has been in game',
    'last': 'Checks when the last game played by Dolphinos was'
}

@bot.command(name='in', help=helper['in'])
async def in_command(ctx):
    in_game = False
    for user in usernames:
        if lol.check_if_ingame(user): 
            in_game = True
    response = "@Dolphinos IS PLAYING LEAGUE OF LEGENDS" if in_game else "The neberizer is not playing league. @Dolphinos, time to come online!"
    await ctx.send(response)

@bot.command(name='time', help=helper['time'])
async def time_command(ctx):
    for user in usernames:
        if lol.check_if_ingame(user):
            await ctx.send("%s has been in game for %d seconds" % (user, lol.get_current_match_time(user)))
            return
    await ctx.send("The bbern is not in a game")

@bot.command(name='last', help=helper['last'])
async def last_command(ctx):
    response = "last game"
    await ctx.send(response)

bot.run(TOKEN)
