import discord
import asyncio
import sys
from config import *

client = discord.Client()
token = sys.argv[1]
spam_text = sys.argv[2]

@client.event
async def on_ready():
    print("Démarrage du spam de texte")
    while not client.is_closed:
        print(spam_texte)
        await client.send_message(discord.Object(id=DiscordSalon), spam_texte)
        await asyncio.sleep(0.7) # Change la vitesse

client.run(token, bot=False)

        




