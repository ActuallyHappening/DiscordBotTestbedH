from __future__ import annotations
import discord
from discord.ext import bridge
from discord.ext import commands

from advanced_gen import AdvancedCommands
from basic_stuff import BasicCommands

from dotenv import dotenv_values, load_dotenv

_secrets = dotenv_values(".env", verbose=True)

intents = discord.Intents.default()
intents.message_content = True

bot = bridge.Bot(
    command_prefix="$", intents=intents)

# Uncomment this line to add the original commands (which are complex :)
# bot.add_cog(AdvancedCommands(bot))

bot.add_cog(BasicCommands(bot))

try:
  bot.run(_secrets["DISCORD_BOT_TOKEN"])
except Exception as e:
  print("ERROR, if shard permissions error please give the bot proper permissions!")
  
  raise e