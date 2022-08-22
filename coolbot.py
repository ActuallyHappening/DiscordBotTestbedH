import math
import random
import discord
from discord.ext import commands

from dotenv import dotenv_values, load_dotenv

_secrets = dotenv_values(".env", verbose=True)

intents = discord.Intents.default()
# intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"), intents=intents)


@bot.command()
async def test(ctx, *args):
    await ctx.send(f"__test__: \n{args}")

@bot.slash_command()
async def random_num(ctx):
    await ctx.send(f"random num between 0 and 6: \n{random.randint(0, 6)}")
    return "what?"

@bot.slash_command()
async def random_num_to_n(ctx, num: int):
    await ctx.send(f"random num between 0 and {num}: \n{random.randint(0, num)}")
    return "is"
    
@bot.slash_command()
async def n_random_nums(ctx, num: int):
    nums = [random.randint(0, 6) for i in range(num)]
    nums_str = "\n".join(map(str, nums))
    await ctx.send(f"{num} random numbers between 0 and 6: \n{nums_str}")
    return "this do?"



bot.run(_secrets["DISCORD_BOT_TOKEN"])