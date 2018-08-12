import discord
import os
import pickle

with open("token", "r") as f:
    TOKEN = f.read()

try:
    f = open("data", "rb")
    count = pickle.load(f)
    f.close()
except FileNotFoundError:
    print("No data found, generating new file.")
    count = 0
    f = open("data", "w")
    f.close()
    pickle.dump(count, open("data", "wb"))

client = discord.Client()

author = "Aeolus#4005"

print(count)

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
            print("test")
            client.close()

    if message.content.startswith('!add'):
        global count
        count += 1
        await client.send_message(message.channel, str(count))


client.start(TOKEN)

print("done")
pickle.dump(count, open("data", "wb"))