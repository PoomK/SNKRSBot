#Bot invite link: https://discord.com/api/oauth2/authorize?client_id=720998084326195200&permissions=0&scope=bot
#SneakerBot Server ID: 720996860554248273

import discord

#Bot server
token = "NzIwOTk4MDg0MzI2MTk1MjAw.XuOIXQ.wcnIgDBzUuOD6GJq0uDDt7ZCiSA"

client = discord.Client()

# @client.event
# async def on_member_join(member):
#     for channel in member.server.channels:
#         if str(channel) == "general":
#             await client.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):

    serverID = client.get_guild(720996860554248273)
    commandChannels = ["commands"]
    coppedChannel = ["copped"]

    if str(message.channel) in commandChannels:
        if message.content.find("!test") != -1:
            await message.channel.send("test completed")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {serverID.member_count}""")
    elif str(message.channel) in coppedChannel:
        if message.content == "!copped":
            await message.channel.send("You copped it :)")

client.run("NzIwOTk4MDg0MzI2MTk1MjAw.XuOIXQ.wcnIgDBzUuOD6GJq0uDDt7ZCiSA")