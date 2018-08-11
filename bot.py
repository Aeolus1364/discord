import discord
import subprocess

TOKEN = 'NDc0NzM2MDc3ODUzMTYzNTIx.DkU1NA.DUc2hPNjpmOrDKFNrcGPAmgD24s'

client = discord.Client()

oof = {}


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    # if message.content.startswith('!search'):
    #     msg = message.content.split(" ")
    #     # if msg[1]
    #     del msg[0]
    #     search = " ".join(msg)
    #
    #     for i in googlesearch.search(search, num=1, stop=10):
    #
    #         await client.send_message(message.channel, i)

    if message.content.startswith('!calc'):
        msg = message.content.split(" ")
        del msg[0]

        a = 0
        print(msg, msg[1])

        one, two = int(msg[0]), int(msg[2])

        if msg[1] == "+":
            a = one + two
        elif msg[1] == "-":
            a = one - two
        elif (msg[1] == "*") or (msg[1] == "x"):
            a = one * two
        elif msg[1] == "/":
            a = one / two
        elif msg[1] == "^":
            if len(str(two)) > 5:
                a = "2 big 4 me"
            else:
                a = one ** two

        await client.send_message(message.channel, str(a))

    if message.content.startswith('!ligma'):
        await client.send_message(message.channel, "Wow, {0.author.mention} is the worst person on the planet.".format(message))

    if "oof" in message.content.lower():
        global oof
        name = message.author
        if name in oof:
            oof[name] += 1
        else:
            oof[name] = 1
            await client.send_message(message.channel, "Congratulations to {0.author.mention} on their first oof!".format(message))

    if message.content.startswith("!oof"):
        await client.send_message(message.channel, "You have oofed {} times!".format(oof[message.author]))

    if message.content.startswith("!python") or message.content.startswith("!y"):
        msg = message.content.split(" ")
        del msg[0]
        msg = " ".join(msg)

        file = open('test.py', 'w')
        file.write(msg)
        file.close()

        cmd = ['python', 'test.py']
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

        d = output.decode('utf-8')

        await client.send_message(message.channel, d)
        print(d)

    if message.content.startswith("!new") or message.content.startswith("!n"):
        msg = message.content.split(" ")
        del msg[0]

        f = open(msg[0], "w")
        f.close()

        await client.send_message(message.channel, "Created new file: {0}".format(msg[0]))

    if message.content.startswith("!edit") or message.content.startswith("!e"):
        msg = message.content.split(" ")
        del msg[0]
        fname = msg[0]
        del msg[0]
        f = open(fname, "w")
        f.write(" ".join(msg))
        f.close()

        await client.send_message(message.channel, "Changes made to: {0}".format(fname))

    if message.content.startswith("!show") or message.content.startswith("!s"):
        msg = message.content.split(" ")
        del msg[0]

        f = open(msg[0], "r")
        msg = f.read()
        f.close()

        await client.send_message(message.channel, msg)

    if message.content.startswith("!run") or message.content.startswith("!r"):
        msg = message.content.split(" ")
        del msg[0]

        cmd = ['python', msg[0]]
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

        d = output.decode('utf-8')

        await client.send_message(message.channel, d)

    # if message.content.startswith("!kill"):
    #     msg = message.content.split(" ")
    #     del msg[0]
    #
    #     if msg[0] == "everything":
    #         for j in client.servers:
    #             for i in j.channels:
    #
    #                 print(j.name, i.name, i.type)
    #                 if i.type == discord.ChannelType.text:
    #                     try:
    #                         await client.send_message(i, "Test message please ignore")
    #                     except discord.errors.Forbidden:
    #                         print(j.name, i.name)

    print(message.author)
    print("{0}: {1}".format(message.author, message.content))


@client.event
async def on_ready():
    print("Connected to ", end="")
    for i in client.servers:
        print(i.name)

client.run(TOKEN)
