# The import functions take code that already exists elsewhere and allow you to use it in your code!
import os
import discord
from dotenv import load_dotenv
import requests
import urllib.request
import datetime
# import shutil

from Get_Screenshot_Data import detect_text_uri
from Google_Sheets import Connect_To_Google_Sheets



# This particular tool requires this driver:
# https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac



# These are global variables, we are able to reference these anywhere in the code without typing the full string
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
DISCORD_SERVER = "Kingdom 2129"

# This is one of the functions we imported, it is used to read a credentials file and keep it secret
load_dotenv()

# A client is also a function we have imported, but this one has a constant use.
client = discord.Client()

# This is the first function we are creating, this does a specific thing chosen by us.
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# This one is a listener, so when something happens elsewhere, it will be called to activate.
@client.event
async def on_message(message):

    if message.content.lower().startswith('bb!'):

        if message.content.lower().__contains__("maria"):
            await message.channel.send(
                "You know, last year I grew the biggest melon in the Shire. Won an award. Called it Maria, lovely thing")

        if message.content.lower().__contains__('wu'):
            await message.channel.send("""Never Laugh At Live Dragons, Bilbo, You Fool!""")

        if message.content.lower().__contains__('abz'):
            await message.channel.send("""Once caught him making off with the spoons!""")

        if message.content.lower().__contains__('wooly'):
            await message.channel.send("""I Don't Know Half Of You Half As Well As I Should Like; 
            And I Like Less Than Half Of You Half As Well As You Deserve.""")

        if message.content.lower().__contains__('ping'):
            await message.channel.send("Bilbo Baggins, at your service!")

        if message.content.lower().__contains__("pong"):
            await message.channel.send("'More Like A Grocer Than A Burglar’ Indeed!")

        if message.content.lower().__contains__('medi'):
            await message.channel.send("""You've been into Farmer Maggot's crops!""")


        if message.content.lower().__contains__('thes'):
            await message.channel.send("""Instead of a dark lord you would have a queen?""")

        if message.content.lower().__contains__('bilbo'):
            await message.channel.send("""That Bilbo Baggins is cracked...""")
            
        if message.content.lower().__contains__('bill'):
            await message.channel.send("""Sold to Frodo for 3 times his worth! 12 silver pennies!""")

        if message.content.lower().__contains__('nightmare'):
            await message.channel.send("""This foe is beyond any of you... RUN!""")
            
        if message.content.lower().__contains__('poo'):
            await message.channel.send("""What a pity that Bilbo did not stab that vile creature, when he had a chance!""")

        if len(message.attachments) > 0:
            # This is to ensure we don't download anything malicious - just pictures, THANK YOU
            count = 0
            stats = []
            for attachment in message.attachments:
                if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    count += 1
                    try:
                        data = detect_text_uri(attachment.url)
                    except:
                        data = {}
                        
                    data['image'] = attachment.url
                    data['discord_user'] = message.author.display_name
                    data['date'] = datetime.datetime.now()

                    stats.append(data)
                    Connect_To_Google_Sheets(stats)

                    await message.channel.send(str(stats))

            await message.channel.send("I've picked up {} attachments".format(count))
            await message.channel.send("More than any Baggins deserves.")



client.run(DISCORD_TOKEN)
