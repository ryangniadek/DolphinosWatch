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
    
    help = "Dolphinos Watch is here to spy on the neberizer himself. REEEEEEEEEEEEEEEEEEEEEEE"

    if message.content == '!DW':
        response = help
        await message.channel.send(response)

client.run(TOKEN)
