from __future__ import annotations
import discord
from discord.ext import bridge
from discord.ext import commands

from advanced_gen import AdvancedCommands
from basic_stuff import BasicCommands

from dotenv import dotenv_values, load_dotenv

# Taking secrets
_secrets = dotenv_values(".env", verbose=True)

# Managing intents
# Asking for permission to like see message content
intents = discord.Intents.default()
intents.message_content = True

# Making the bot class
# which manages everything under the hood
bot = bridge.Bot(
    command_prefix="$", intents=intents)

# Uncomment this line to add the original commands (which are complex :)
# bot.add_cog(AdvancedCommands(bot))

# Add the commands we want
bot.add_cog(BasicCommands(bot))

try:
  print("Beginning ...")
  bot.run(_secrets["DISCORD_BOT_TOKEN"])
except Exception as e:
  print("ERROR, if shard permissions error please give the bot proper permissions!")
  
  raise e