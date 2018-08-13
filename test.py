import discord
from discord.ext import commands

with open("token", "r") as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="your mother"))
    print('Bot is ready')


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='test')
    await client.add_roles(member, role)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []

    try:
        amount = int(amount)
    except ValueError:
        amount = 1

    amount += 1

    async for message in client.logs_from(channel, amount):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Deleted {} messages.'.format(amount - 1))



client.run(TOKEN)

