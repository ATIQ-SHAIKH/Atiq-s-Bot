import discord
import os
import requests
import json
from Alive import keep_alive

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+"  -" + json_data[0]['a']
    return(quote)

@client.event

async def on_ready():
    print("We have logged in.....")
    print("Bot online!!!")
    quote = get_quote()
    daily_quotes_channel = client.get_channel(819980892155936790)
    await daily_quotes_channel.send('@everyone Here is an amazing quote I found...')
    await daily_quotes_channel.send(quote)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('+hello'):
        await message.channel.send('Hello Bitch!')
    if message.content.startswith('+quote'):
        quote = get_quote()
        await message.channel.send(quote)

keep_alive()
client.run('ODE2MjgwNTUzODc5MTA5NjYy.YD4qgQ.9e_h5eNCI91PfAe9SPh6YJ8oBBo')

