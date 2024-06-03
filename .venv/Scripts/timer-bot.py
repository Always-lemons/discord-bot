import discord
import time
import datetime
import asyncio

from discord.ext import commands

async def timer(timer_h, timer_m, timer_s, ):
    total_sec = timer_h * 3600 + timer_m * 60 + timer_s
    while total_sec > 0:
        timer = datetime.timedelta(seconds = total_sec)
        print(total_sec)
        await asyncio.sleep(1)
        total_sec -= 1

class MyClient(discord.Client):
 async  def on_ready(self):
        print(f'Logged in as {self.user}!')
 async def on_message(self,message):
        print(f'Message from:{message.guild.id} : {message.author}: {message.content}')

        if message.author.id == self.user.id:  #makes sure the bot wont respond to itself
            return

        if message.content.casefold().startswith(morn_string):  #Makes bot respond to morning fams
            await message.reply('Morning Fam')

        if message.content.startswith(timer_string):
            total_timer = message.content.replace(' ','') # get rid of spaces in string
            if len(total_timer) == 8 : # Check to see if the right # of characters have been entered
                num_check = total_timer[2:8]
                if num_check.isnumeric() == False :
                    await message.reply('Only use Numbers, Thanks!')
                    return
                timer_h = int(total_timer[2:4])
                timer_m = int(total_timer[4:6])
                timer_s = int(total_timer[6:8])
                print(f'Timer Hr: {timer_h} Timer min: {timer_m} Timer sec:{timer_s}')
                await message.reply(f'Timer Hours: {timer_h} Minutes: {timer_m}  Seconds:{timer_s} SET')
                await timer(timer_h, timer_m, timer_s)   #wait for timer loop to finish then reply with end message
                await message.reply ('TIMES UP')
            if len(total_timer) != 8 :
                await message.reply('Timer requires HH MM SS format')

timer_string = "!T"
morn_string = 'morning fam'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)
client.run('TOKEN')
#