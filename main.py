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
    if  message.author==client.user:
        return

    if message.content.startswith("$hello"):
          await message.channel.send("Hello!")

    if message.content=="$timer":
          await message.channel.send("Please set timer '$timer.min for min, $timer.sec    for seconds ")

    if message.content.startswith("$timer.min"):
          süre = int(message.content[10:]) * 60
          print(countdown(süre))
          await message.channel.send("Süre doldu hadi geçmiş olsun")

    if message.content.startswith("$timer.sec"):
          süre = int(message.content[10:]) 
          print(countdown(süre))
          await message.channel.send("Süre doldu hadi geçmiş olsun")    



    



client.run(os.getenv("TOKEN"))
