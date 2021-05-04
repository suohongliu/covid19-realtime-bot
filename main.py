import discord
import os
import get_data as g

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ottawa'):
        data = g.daily_cases()

        #find user with id
        kyle = await client.fetch_user(139539313397334017)

        await message.channel.send(kyle.mention)

        #method 2 to mention user with userID
        '''
        await message.channel.send('<@139539313397334017>')
        '''

        myStr = ""
        for k, v in data.items():
            myStr += k + ': ' + str(v) + "\n"
        await message.channel.send(myStr)


client.run(os.getenv('TOKEN'))
