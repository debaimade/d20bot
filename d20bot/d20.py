'''
A simple discord bot made to roll a 20 sided die. 
Built and modified from the tutorials at devdungeon
https://www.devdungeon.com/content/make-discord-bot-python
'''
import discord
import os
import random

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!roll'):
        side = random.randint(1,20)
        response = 'You rolled a ' + str(side)
        msg = response.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!fortune'):
        fortunes_dir = 'fortune'
        fortunes = []
        
        for fortune_file in os.listdir(fortunes_dir):
            fortune_fh = open(os.path.join(fortunes_dir, fortune_file), 'r')
            fortunes.extend(fortune_fh.read().split("\n%\n"))
        
        response = random.choice(fortunes)
        msg = response.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


token_fh = open('token.cfg','r')
TOKEN = token_fh.readline().rstrip()
client.run(TOKEN)
