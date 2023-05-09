import discord

TOKEN = 'MTEwNTE5NjU1ODg4ODIwNjQ3Nw.GN5VXP.1e1Xpw2OIUnstl5cC7T7reCjcAX3A4iT_I4MY4'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
send = False
print("hello")
@client.event
async def on_ready():
  print(f'{client.user} is now running!')

@client.event
async def on_message(message):
  if message.author == client.user or send:
    return
  send = True
  msg = await message.channel.send("0")
  i = 1
  while i < 1000000000000000000000:
    await msg.edit(content = f"{i}")
    i= i+1
