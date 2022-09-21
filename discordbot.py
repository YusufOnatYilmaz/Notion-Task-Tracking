from discord.ext import commands, tasks

from constants import *

import read_database

TOKEN = DISCORD_BOT_TOKEN

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@tasks.loop(seconds=30)
async def called_once_a_day():
    user = await bot.fetch_user(USER_ID)
    response = read_database.retrieve_database()
    await user.send(response)

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run(TOKEN)