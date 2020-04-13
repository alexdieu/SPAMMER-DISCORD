import urllib.request
import discord
import asyncio
from config import *
from translate import Translator
import sys
from bs4 import BeautifulSoup


client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    while not client.is_closed:
        html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
        soup = BeautifulSoup(html,"html.parser")
        insultes_texte = soup.find('h1')
        translator= Translator(from_lang="english",to_lang="french")
        translation = translator.translate("insultes_texte")
        print(insultes_texte.text)
        await client.send_message(discord.Object(id=DiscordSalon), insultes_texte.text)
        await asyncio.sleep(0.7) # Change la vitesse de post
    
print(token)    
client.run(token,bot=False)
