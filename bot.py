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
usernames = [lol.get_summoner('dolphinos'), lol.get_summoner('LHemisphere'), lol.get_summoner('neberizer')]
helper = {
    'in': 'Checks if dolphinos is in a game on any of his accounts. Pass an optional paramter to check for another user.',
    'time': 'Checks how long dolphinos has been in game',
    'last': 'Checks when the last game played by Dolphinos was',
    'hours': 'Checks the amount of hours that Dolphinos has been in game over the specified timespan (given as argument in hours)'
}

@bot.event
async def on_command_error(ctx, error):
    response = 'Congrats, '
    if isinstance(error, commands.CommandNotFound):
        response = 'The command %s does not exist. Sorry not sorry.' % ctx
    elif isinstance(error, commands.CommandError):
        response = 'The command %s was not called correctly, check the help page' % ctx
    await ctx.send(response)

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


@bot.command(name='hours', help=helper['hours'])
async def hours_command(ctx, span: int):
    seconds = 0
    for user in usernames:
        seconds += lol.get_timeplayed(user, span)
    hours = seconds / 3600
    percent = (hours / span) * 100
    response = "Over the last %d hours, Dolphinos has played league for %d hours. Thus, he has spend %d percent of his time playing league." % (span, hours, percent)
    await ctx.send(response)

bot.run(TOKEN)
