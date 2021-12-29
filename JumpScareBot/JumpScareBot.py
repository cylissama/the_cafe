#---Cy Dixon FazBot---#

import os
import random
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
load_dotenv()

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print("-----------------------------------")
    print("FazBot is fully functional!")
    print("-----------------------------------")
    print("                             ╓▄████████▄                                    ")
    print("                             ███████████                                    ")
    print("                            ████████▓██                                    ")
    print("                ,╓╓,        ███████████     ╓▓▓██▓▓▓╗                      ")
    print("              g▓▓███▓▓@     ███████████▄   ▓▓▓▓▓▓██▓▓                      ")
    print("             ╟▓▓▓▓▓▓██▓╣ ▄████████████████╖▓▓▓▓╢╢▓▓▓▓U                     ")
    print("             ▓▓▓▓╣╢▓▓▓▓▓▄███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓Ñ                      ")
    print("              ╙▓▓▓▓▓▓███████▓▓▓▓▓▓▓██████▓▓▓▓▓██▓▀▀                        ")
    print("                  ╙╜║▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓,                          ")
    print("                   ▓█▓▓▓█████╣▓▓▓▓███▓▓▓▓▓╣▓▓▓▓▓▓,                         ")
    print("                  ▐█▓▓█▓▓▀▀▀▀▓▓▓╣▓█▓▓''`╙╙▓╫▓▓▓▓▓▓                         ")
    print("                  ╓██▓▓██▓@,╓ƒ▓▓▓▓▓██▓░   j▓▓▓▓▓▓▓█╦                        ")
    print("                  ▓██▓▓██▓▓████████▓▒▒╬@@╬╣▓▓▓▓▓▓▓▓▓                        ")
    print("                 ╓▓▓▓▓▓╣▓▌▒██████▀▒▓╣╢╣╢╢╢▓▓▓▓▓▓▓▓█▓          .,            ")
    print("                 ╠▓▓▓▓▓▓▓▓╣╣╣╣╢╣╢╢▓▌╣▓▓╢╢╢╢▓▓▓▓▓▓▓█▓         ╓▓▓▓@  ,       ")
    print("                 -╠▓█▓▓▓▓╢╢╢╢╢▓▓▓▓╢╢╢╢╢╢╢▓▓▓▓▓▓▓▓▓╜          ████`▐▓▓▓▓     ")
    print("                   ╙▀██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████▓U         ▓███╩▐████`▄▓▓▄ ")
    print("                     ██████████████████████████▓▓▓ ╓▓▓▄▄   ▓▓▓█▌▄███▓,▓███▀ ")
    print("                    ▓███████████████████████▓▓▓█▌ ╠███▓▓▓▓▓▓▓▓▓▓▓█▌╓████╜  ")
    print("          █▓▀████▄  ▐██████████████████████▓▓▓█▌   ╙███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓`   ")
    print("         ███▌▒████▌ ██▓@▄▄░,▐▒╓╓▄╓╓▄@╬▓▓▓██▓▓█▌      ▀████████▓▓▓▓▓▓█▀     ")
    print("  ,,╓   ╓█████████▌ █▓▓▓▓▓▓▓▓▓▓▓╢╢╣╫▓▓▓▓▓▓███╩         ▀█████████▓▓▓╜      ")


@client.command(pass_context = True)
async def activate(ctx):
    if(ctx.author.voice):
        await ctx.send("Freddy is on the hunt!")
        channel = ctx.message.author.voice.channel
        while (True):
            
            
            voice = await channel.connect()
            source = FFmpegPCMAudio('scare1.wav')
            player = voice.play(source)

            await asyncio.sleep(5)

            await ctx.guild.voice_client.disconnect()

            await asyncio.sleep(random.randint(30,300))

            
            voice = await channel.connect()
            source = FFmpegPCMAudio('scare2.mp3')
            player = voice.play(source)

            await asyncio.sleep(5)

            await ctx.guild.voice_client.disconnect()

            await asyncio.sleep(random.randint(60,500))

            
            voice = await channel.connect()
            source = FFmpegPCMAudio('scare3.mp3')
            player = voice.play(source)

            await asyncio.sleep(5)

            await ctx.guild.voice_client.disconnect()

            await asyncio.sleep(random.randint(30,300))
    else:

        await ctx.send("User must be inside a voice channel")


@client.command(pass_context = True)
async def dismantle(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("See you soon!")
    await ctx.bot.logout()

client.run(os.getenv("TOKEN"))