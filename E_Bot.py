# Class bot

import discord
from discord.ext import commands
import random, os

#Intensts
intents = discord.Intents.default()
intents.message_content = True

#Bot variables
bot = commands.Bot(command_prefix='$', intents=intents)

#Bot commands

@bot.event                         #Bot will know if something happened
async def on_ready():              #If bot is ready
    print('Bot ready!')

@bot.command()                     #Command that will command for bot
async def handwork(ctx):
    img_name = random.choice(os.listdir(handwork))
    with open(f'Handworkd/{img_name}', 'rb') as image:      # Open image and keep it in variable
        picture = discord.file(image)
    await ctx.send(picture)

bot.run('Your Token') # Bot Token
