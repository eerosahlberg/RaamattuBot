import os
import random
from time import sleep

import discord
from dotenv import load_dotenv

from urllib.request import urlopen

url = 'https://raamattu.fi/raamattu/KR92/MAT/'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

IsaMeidan = ['Isä meidän, joka olet taivaissa.',
            'Pyhitetty olkoon sinun nimesi.',
            'Tulkoon sinun valtakuntasi.',
            'Tapahtukoon sinun tahtosi,',
            'myös maan päällä niin kuin taivaassa.',
            'Anna meille tänä päivänä meidän jokapäiväinen leipämme.',
            'Ja anna meille meidän syntimme anteeksi,',
            'niin kuin mekin anteeksi annamme niille,',
            'jotka ovat meitä vastaan rikkoneet.',
            'Äläkä saata meitä kiusaukseen,',
            'vaan päästä meidät pahasta.',
            'Sillä sinun on valtakunta ja voima ja kunnia iankaikkisesti.',
            '<:Vilkuttava_Kaataja:842673621456388106> Aamen. <:Vilkuttava_Kaataja2:842673923535405058>']

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    await client.change_presence(activity=discord.Game('Raamattu 2'))
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(scrape())
    # channel = client.get_channel(787981416490074112)

@client.event
async def on_message(message):
    if message.content == 'jumalan siunausta' :

        await message.channel.send('Samoin!')
        print(scrape())
    if (message.content == 'lue raamattua' or message.content == 'Lue raamattua'):

        await message.channel.send("<:Vilkuttava_Kaataja:842673621456388106>" + scrape() + "<:Vilkuttava_Kaataja2:842673923535405058>")
        print(scrape())
    if message.content == 'rukoilkaamme':
        for i in range(len(IsaMeidan)):
            await message.channel.send(IsaMeidan[i])
            sleep(1)

def scrape():

    book_index = random.randint(1, 28)
    verse_index = random.randint(1,30)

    url = 'https://raamattu.fi/raamattu/KR92/MAT.' + str(book_index)
    verse = 'data-verse-org-id="MAT.' + str(book_index) + "." + str(verse_index) + '"'


    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")


    x=0
    
    if(html.find(verse) == -1):
        while(x == 0):
            verse = 'data-verse-org-id="MAT.' + str(book_index) + "." + str(random.randint(1,30)) + '"'
            #verse = 'data-verse-org-id="MAT.2.1"'
            if(html.find(verse) != -1):
                x=1

   
    start_index = html.find(verse) + len(verse) + 1
    end_index = html.find('</span>', start_index)
    title = html[start_index:end_index]

    while(html.find(verse, end_index) > -1):
        start_index = html.find(verse, end_index) + len(verse) + 1
        end_index = html.find('</span>', start_index)
        title += html[start_index:end_index]
        print(end_index)
        sleep(0.5)

    return title


client.run(TOKEN)
