import os
import discord
import time

client = discord.Client()



  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    return t
  
  



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$timer"):
        await message.channel.send("Please set timer '$set.timer (your time here in seconds)'")

    if message.content.startswith("$set.timer"):
        süre = int(message.content[10:])
        print(countdown(süre))
        await message.channel.send("Süre doldu hadi geçmiş olsun")


    



client.run(os.getenv("TOKEN"))
