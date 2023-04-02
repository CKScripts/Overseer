import interactions
import os

Core = os.listdir("../CKSB-Assist/Core/Core.py")

from Core import Bot

@Bot.command(
  name = "lookup",
  description = "Lookup a player's data on the database",
  options = [
    interactions.Option(
      name  = "username",
      description  = "The Username of the player",
      type  = interactions.OptionType.STRING,
      required  = True,
    ),
  ],
)

async def lookup(Context: interactions.CommandContext,username: str):
  await Context.send(f"Attempting to lookup {username}..")