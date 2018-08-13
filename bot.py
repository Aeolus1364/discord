import discord
from discord.ext import commands
import pickle
import bug

with open("token", "r") as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix='!')
try:
    users = pickle.load(open('data', 'rb'))
except FileNotFoundError:
    users = {}
creator = open("creator", "r").read()


def s(text):
    return "`{}`".format(text)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with fire"))
    print("Connected to the following servers:")
    for i in client.servers:
        print("\t", i)


@client.event
async def on_message(msg):
    content = msg.content
    author = msg.author
    print(author, client.user)
    if not author == client.user:
        if author not in users:
            users[author] = {'oof': 0, 'bug': bug.Bug()}

        if author != client.user and not content.count("!oof"):
            num = content.count('oof')
            if num > 0:
                users[msg.author]['oof'] += num

        users[author]['bug'].digest(content)

    await client.process_commands(msg)


@client.command(pass_context=True)
async def oof(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    await client.say("{} ".format(member.mention) + s("has oofed {} times!".format(users[member]['oof'])))


@client.command(pass_context=True, name="b", aliases=["bug"])
async def b(ctx, *args):
    author = ctx.message.author
    bug = users[author]['bug']
    nargs = len(args)
    if args[0] == "name":
        if nargs >= 2:
            bug.name = args[1]
            await client.say(s("Your bug's name has been changed to") + " " + users[author]['bug'].name)

        else:
            await client.say(s("Your bug's name is") + " " + users[author]['bug'].name)
    elif args[0] == "word":
        count = 0
        word = ""
        for w in bug.words:
            num = bug.words[w]
            if num > count:
                count = num
                word = w
        await client.say(s("Your most used word is {}".format(word)))
    elif args[0] == "clear":
        bug.words = {}
        await client.say(s("Your words have been erased."))


@client.command(pass_context=True)
async def stop(ctx):
    if str(ctx.message.author) == creator:
        await client.say(s("Shutting down..."))
        pickle.dump(users, open('data', 'wb'))
        await client.logout()
    else:
        await client.say(s("Nice try buckaroo."))


client.run(TOKEN)
