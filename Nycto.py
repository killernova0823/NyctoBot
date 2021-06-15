import discord
from discord import member
import asyncio
import time

messages = joined = 0


client = discord.Client()

async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

@client.event
async def on_member_join(member, mention:member):
    for channel in member.guild.channels:
     if str(channel)=="commands":
        await channel.send_message(f"""Welcome me to the server{mention.member}""")

@client.event 
async def on_message(message):
    id = client.get_guild(819993683062554655)

    if message.content.find("thanks.") != -1:
        await message.channel.send("Welcome")
    elif message.content.find("hello.") != -1:
        await message.channel.send("Hi")
    elif message.content.find("help.") != -1:
        await message.channel.send("Type ContactDEV. to DM Developer")
    elif message.content.find("Developer.") != -1:
        await message.channel.send("Prashant Kumawat")
    elif message.content.find("Serverinfo.") != -1:
        await message.channel.send(f"""Number of Members in server: {id.member_count}""")



client.loop.create_task(update_stats())
client.run("ODQ1NTY0MzgyNDU2OTcxMjc0.YKizMg.xo4BLoQZRPjVa4wNPlQtwIlHjSA")
