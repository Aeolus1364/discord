import discord
import os
with open("token", "r") as f:
    TOKEN = f.read()

client = discord.Client()

author = "Aeolus#4005"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.servers)
    print('------')


@client.event
async def on_message(message):
    global author
    if message.content.startswith('!stop'):
        if str(message.author) == author:
            quit()


client.run(TOKEN)