from __future__ import annotations
import math
import random
from typing import Tuple
import discord
from discord.ext import bridge
from discord.ext import commands

from dotenv import dotenv_values, load_dotenv

_secrets = dotenv_values(".env", verbose=True)

intents = discord.Intents.default()
# intents.message_content = True

bot = bridge.Bot(
    command_prefix="$", intents=intents)

_previousNums = []
_defaultLowNum = 0
_defaultHighNum = 6

def _gen_num(low: int | Ellipsis = ..., high: int | Ellipsis = ...) -> Tuple[int, int]:
  low = low if low is not Ellipsis else _defaultLowNum # provide defaults
  high = high if high is not Ellipsis else _defaultHighNum # provide defaults
  _num = random.randint(low, high)
  _previousNums.append(_num)
  return (_num, len(_previousNums))

def _gen_prefix(a: int) -> str:
  if str(a).endswith("1"):
    return "st"
  elif str(a).endswith("2"):
    return "nd"
  elif str(a).endswith("3"):
    return "rd"
  else:
    return "th"

async def _int(ctx, x: str) -> int:
  try:
    return int(x)
  except ValueError:
    await ctx.send(f"**{x}** is not a valid number")

@bot.bridge_command()
async def test(ctx):
    await ctx.send(f"__test__")

@bot.bridge_command()
async def gen_random_num(ctx):
    await ctx.send(f"random num between 0 and 6: \n{_gen_num()[0]}")
    return "what?"

@bot.bridge_command()
async def gen_random_num_to(ctx, num):
    num: int = await _int(num)
    _num = _gen_num(..., num)
    await ctx.send(f"{_num[1]}{_gen_prefix(_num[1])} random num is: \n**{_num[0]}**")
    return "is"

    
@bot.bridge_command()
async def gen_n_random_nums(ctx, num):
    num: int = await _int(ctx, num)
    assert num > 0 # Errors otherwise
    _nums = [_gen_num(..., ...) for i in range(num)]
    nums_str = "\t".join(map(lambda n: str(n[0]), _nums))
    _beginning_prefix = f"{_nums[0][1]}{_gen_prefix(_nums[0][1])}"
    _ending_prefix = f"{_nums[-1][1]}{_gen_prefix(_nums[-1][1])}"
    await ctx.send(f"{_beginning_prefix} to {_ending_prefix} random numbers: \n{nums_str}")

@bot.bridge_command()
async def history(ctx):
    _string = ""
    for i, num in enumerate(_previousNums):
      _string += f"{i}{_gen_prefix(i)}: {num}\n"
    if _string != "":
      await ctx.send(f"History random numbers: \n{_string}")
    else:
        await ctx.send(f"History is empty! May have /clear ed history")

@bot.bridge_command()
async def clear_history(ctx):
    _previousNums.clear()
    await ctx.send("History cleared :smile:")

try:
  bot.run(_secrets["DISCORD_BOT_TOKEN"])
except Exception as e:
  print("ERROR, if shard permissions error please give the bot permissions!")
  
  raise e