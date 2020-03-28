# Discord Bot for Monitoring Dolphinos written in Python
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif 'DW!' not in message.content:
        return  
    elif 'info' in message.content:
        response = "Named for our favorite League of Legends player, Dolphinos Watch alerts us all of Dolphinos' activity in game. Commands are:\n`DW!info - give information about the bot\nDW!in - check if dolphinos is in game\nDW!time - time played in the last 24 hours\nDW!last - the last game dolpinos has played`"
        await message.channel.send(response)
    elif 'in' in message.content:
        response = "in placeholder"
        await message.channel.send(response)
    elif 'time' in message.content:
        response = "time in game"
        await message.channel.send(response)
    elif 'last' in message.content:
        response = "last game"
        await message.channel.send(response)


client.run(TOKEN)
