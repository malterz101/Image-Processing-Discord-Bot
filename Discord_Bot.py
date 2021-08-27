# The import functions take code that already exists elsewhere and allow you to use it in your code!
import os
import discord
from dotenv import load_dotenv
import requests
import urllib.request
import datetime
# import shutil

from Get_Screenshot_Data import extract_stats
from Google_Sheets import Connect_To_Google_Sheets



# This particular tool requires this driver:
# https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac



# These are global variables, we are able to reference these anywhere in the code without typing the full string
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", input("Add token manually"))
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

        if message.content.lower().__contains__('donc'):
            await message.channel.send("""Once caught him making off with the spoons!""")

        if message.content.lower().__contains__('wooly'):
            await message.channel.send("""I Don't Know Half Of You Half As Well As I Should Like; 
            And I Like Less Than Half Of You Half As Well As You Deserve.""")

        if message.content.lower().__contains__('ping'):
            await message.channel.send("Bilbo Baggins, at your service!")

        if message.content.lower().__contains__("pong"):
            await message.channel.send("'More Like A Grocer Than A Burglar’ Indeed!")

        if message.content.lower().__contains__('Medi'):
            await message.channel.send("""You've been into Farmer Maggot's crops!""")


        if message.content.lower().__contains__('Thes'):
            await message.channel.send("""Instead of a dark lord you would have a queen?""")

        if message.content.lower().__contains__('Bilbo'):
            await message.channel.send("""That Bilbo Baggins is cracked...""")

        if len(message.attachments) > 0:
            # This is to ensure we don't download anything malicious - just pictures, THANK YOU
            count = 0
            stats = None
            for attachment in message.attachments:
                if attachment.filename.__contains__('png'):
                    count += 1
                    # image_loc = "screenshots/ss-{}-{}.jpg".format(
                    #     datetime.datetime.now(),
                    #     count
                    # )
                    #
                    # r = requests.get(attachment.url, stream=True)
                    #
                    # with open(image_loc, "wb") as out_file:
                    #     # shutil.copyfileobj(r.raw, out_file)
                    #     print('')
                    #
                    # try:
                    #     stats = extract_stats(image_loc)
                    # except Exception as e:
                    #     print(e)
                    #     await message.channel.send("Bother burgling and everything to do with it!")

                    stats[0]['image'] = attachment.url
                    stats[0]['discord_user'] = message.author.display_name
                    #stats[0]['discord_id'] = message.author.user.id
                    Connect_To_Google_Sheets(stats)

                    # await message.channel.send(str(stats))

            await message.channel.send("I've picked up {} attachments".format(count))
            await message.channel.send("More than any Baggins deserves.")



# Everything above just tells the program how to run, this actually sets the whole thing off.

client.run(DISCORD_TOKEN)