from __future__ import annotations
import random
import textwrap
from types import EllipsisType
from typing import Tuple
from discord.ext import bridge, commands


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
    await ctx.send(f"ERROR: **{x}** is not a valid number!")

class AdvancedCommands(commands.Cog):
  _previousNums = []
  _defaultLowNum = 0
  _defaultHighNum = 6
  
  def _gen_num(self, low: int | EllipsisType = ..., high: int | EllipsisType = ...) -> "Tuple[int, int]":
    low = low if low is not Ellipsis else _defaultLowNum # provide defaults
    high = high if high is not Ellipsis else _defaultHighNum # provide defaults
    _num = random.randint(low, high)
    self._previousNums.append(_num)
    return (_num, len(self._previousNums))
  
  @bridge.bridge_command()
  async def gen_random_num(self, ctx):
      await ctx.respond(f"Generated a random num between {self._defaultLowNum} and {self._defaultHighNum}: \n{self._gen_num()[0]}")

  @bridge.bridge_command()
  async def gen_random_num_to(self, ctx, num):
      num: int = await _int(ctx, num)
      _num = self._gen_num(..., num)
      await ctx.respond(f"{_num[1]}{_gen_prefix(_num[1])} random num is: \n**{_num[0]}**")
      
  @bridge.bridge_command()
  async def gen_n_random_nums(self, ctx, num):
      num: int = await _int(ctx, num)
      assert num > 0 # Errors otherwise
      _nums = [self._gen_num() for i in range(num)]
      nums_str = textwrap.fill(", ".join(map(lambda n: str(n[0]), _nums)), 30)
      _beginning_prefix = f"{_nums[0][1]}{_gen_prefix(_nums[0][1])}"
      _ending_prefix = f"{_nums[-1][1]}{_gen_prefix(_nums[-1][1])}"
      await ctx.respond(f"{_beginning_prefix} to {_ending_prefix} random numbers: \n{nums_str}")

  @bridge.bridge_command()
  async def set_default_low_num(self, ctx, num):
      num: int = await _int(ctx, num)
      global _defaultLowNum
      _defaultLowNum = num
      await ctx.respond(f"Default low number is now: {_defaultLowNum}\nNow, random numbers will be within the range of [{_defaultLowNum}, {_defaultHighNum}]")

  @bridge.bridge_command()
  async def set_default_high_num(self, ctx, num):
      num: int = await _int(ctx, num)
      global _defaultHighNum
      _defaultHighNum = num
      await ctx.respond(f"Default high number is now: {_defaultHighNum}\nNow, random numbers will be within the range of [{_defaultLowNum}, {_defaultHighNum}]")

  @bridge.bridge_command()
  async def reset_defaults(self, ctx):
      global _defaultLowNum, _defaultHighNum
      _defaultLowNum = 0
      _defaultHighNum = 6
      await ctx.respond(f"Defaults have been reset to: [{_defaultLowNum}, {_defaultHighNum}]")
  
  @bridge.bridge_command()
  async def test(self, ctx):
      await ctx.respond(f"__test__")

  @bridge.bridge_command()
  async def history(self, ctx):
      _string = ""
      for i, num in enumerate(self._previousNums):
        # Indexes start at 0, but we want to start at 1 for '1st', '2nd', etc. not '0th', '1st', etc.
        i += 1 
        _string += textwrap.fill(f"**{i}**{_gen_prefix(i)}: {num},", width=60)
        _string += " "
      if _string != "":
        await ctx.respond(f"History random numbers: \n{_string}")
      else:
          await ctx.respond(f"History is empty! May have /clear ed history")

  @bridge.bridge_command()
  async def clear_history(self, ctx):
      self._previousNums.clear()
      await ctx.respond("History cleared :smile:")
  
def setup(bot):
  bot.add_cog(AdvancedCommands)