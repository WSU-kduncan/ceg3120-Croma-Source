
# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Destiny_quotes = [
        "Whether we wanted it or not, we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather he commands the Siege Dancers from an Imperial Land Tank outside of Rubicon. Hes well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold. -Zavala",
	"WHAT DO YOU MEAN YOU CAN'T CONCENTRATE WHEN I'M YELLING? RELAX! -Shaxx",
	"You're Not Brave. You've Merely Forgotten The Fear Of Death. Allow Me To Reacquaint You. -Ghaul",
    ]
    if message.content == "Destiny":
    #if message.content.startswith('$Destiny'):
        response = random.choice(Destiny_quotes)
        await message.channel.send(response)

client.run(TOKEN)
