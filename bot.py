import discord
from discord.ext import commands
from discord.utils import get
#import youtube_dl
import os

# ********************************************************************************************************
client = discord.Client()

# ********************************************************************************************************

# Welcome Users to Channel
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "thetavern": # we check to make sure we're sending messages in specific channel
            await channel.send_message(f"""Welcome to the server {member.mention}""")
    
# ********************************************************************************************************

@client.event
async def on_message(message):

    id = client.get_guild(548381331684589578)
    channels = ["thetavern", "nsfw-antiwholesome", "miras-wholesome-channel", "east_asian_casino"]

    # Checks if in correct channel; Restricting Channels
    if str(message.channel) in channels:

        # If the user says $hello we will send back hi
        if message.content.find("$hello") != -1:
            await message.channel.send("Hello Kazuma-kun!")

        # If the user says $users we will send back the members in discord group
        if message.content == "$users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        # We cann use id.member_count

# ********************************************************************************************************
#@commands.command(pass_context=True)
#async def hug(self, ctx):
   # await self.bot.say("hugs {}".format(ctx.message.author.mention()))

# ********************************************************************************************************
client.run('NzI3MjkyOTYxMzgwODkyNzkz.Xvpv6Q.AqdgL8oxUSo4p2n_s6TUdl0pAVw')