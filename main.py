# this is just boilerplate code from whnat we did last time, modify it

import discord
from discord.ext import commands
client = discord.Client()

client = commands.Bot(command_prefix = "!")

#commands
@client.event
async def on_ready():
<<<<<<< HEAD
    general_channel = client.get_channel(805633741166477365) #put client ID here
    #await general_channel.send(hackernews_module.tophn_wrapper(0))
    #await general_channel.send('!warn @animated')

@client.command()
async def opgg(ctx):
	await ctx.send('https://op.gg')

@client.command()
async def warn(ctx):
    await ctx.send('https://tenor.com/view/discord-meme-spooked-scared-mod-gif-18361254')

@client.command()
async def args(ctx, arg1, arg2):
    await bot.say('You sent {} and {}'.format(arg1, arg2))

client.run('ODQwNjIxMTQ2MDgzOTUwNjIy.YJa3cw.xVXFwH8_3rmos_V3qsoZnIl3u1k') #put discord bot token here
=======
    general_channel = client.get_channel(ClientID) #put client ID here
    await general_channel.send('@EGG')

client.run('Token') #put discord bot token here

>>>>>>> f933cb3052fa8742af21e2dbbced05932ce13fca
