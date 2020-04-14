import discord
import asyncio
import random
import os
import sys
from config import *

client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    print("Image Spammer démarre")
    while not client.is_closed:
            UpImage = random.choice(os.listdir(Images)) 
            print(UpImage)
            await client.send_file(discord.Object(id=DiscordSalon), Images + UpImage)
            await asyncio.sleep(0.7) # Change la vitesse à laquelle les images sont affichées

client.run(token, bot=False)
