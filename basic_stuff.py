from __future__ import annotations
import random
from typing import List
from discord.ext import commands, bridge

decorator = bridge.bridge_command

class BasicCommands(commands.Cog):
  _roulette_history: "List[int]" = []
  _slot_machine_history: "List[List[int]]" = []
  
  
  @decorator(description="Play roulette! Spin to generate a random number between 0 and 6")
  async def roulette(self, ctx):
    _num = random.randint(0, 6) # Generate random number
    self._roulette_history.append(_num) # Add to history list
    ctx.respond(f"Roulette spun the number {_num}!")

  @decorator(description="Try your luck at the slot machine! Enter to generate 4 random numbers between 0 and 6")
  async def slot_machine(self, ctx):
    _nums = [random.randint(0, 6) for i in range(4)] # Generate a list of 4 random numbers
    self._roulette_history.append(_nums) # Add to history
    ctx.respond(f"Slot machine spun up **{_nums[0]}**, **{_nums[1]}**, **{_nums[2]}**, and **{_nums[3]}**!")
  
  @decorator()
  async def roulette_history(self, ctx):
      ctx.respond(f"Roulette history: {self._roulette_history}") # TODO: Does not output very pretty :(
  
  @decorator()
  async def slot_machine_history(self, ctx):
      ctx.respond(f"Slot machine history: {self._slow_machine_history}") # TODO: Does not output very pretty :(
  