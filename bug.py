from __future__ import annotations
import discord
from discord.ext import bridge
import pretty_traceback
pretty_traceback.install()

bot = bridge.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.bridge_command()
async def test(ctx, num: int):
    await ctx.send(f"__test__ {num=}")