import interactions
import os

CommandsPath = "../CKSB-Assist/Core/Commands"
Commands = os.listdir(CommandsPath)

Data = {
  "Token": os.environ["Token"],
  "Guild ID": 1089395287891640450,
}

Bot = interactions.Client(
  token = Data["Token"],
  default_scope = Data["Guild ID"],
)

for Command in Commands:
     print(Command)
  
Bot.start()