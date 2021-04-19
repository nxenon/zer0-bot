#!/usr/bin/env python3

'''
Zer0 Discord Bot
'''

import discord

try:
    with open('token.txt','r') as token_file:
        token = token_file.read()

except FileNotFoundError:
    with open('token.txt','w') as token_file:
        print('put the token inside token.txt file')
        exit()

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {}'.format(client.user))

@client.event
async def on_message(message):
    print(message.content)

    message.content = message.content.lower()

    if message.content.startswith('z!'):

        if message.content == 'z! ping':
            await message.channel.send("I'm alive :)")

        elif message.content == 'z! info':
            await message.channel.send('Zer0 Bot')

client.run(token)