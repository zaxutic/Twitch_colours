import datetime
import json
from pathlib import Path

import twitchio
from twitchio.ext import commands
try:
    from termcolor import colored
except ModuleNotFoundError:
    def colored(*args, **kwargs):
        return args[0]

from config import auth


def current_time():
    t = datetime.datetime.now()
    return colored(t.strftime("%d/%m %H:%M:%S"), "green")


class Bot(commands.Bot):

    def __init__(self):
        self.colours = [
            "Red", "Firebrick", "Chocolate", "OrangeRed", "Coral",
            "GoldenRod", "YellowGreen", "Green", "SeaGreen", "SpringGreen",
            "DodgerBlue", "Blue", "BlueViolet", "HotPink"
        ]
        self.count = 0

        self.channel_path = Path.cwd().joinpath("config", "channels.json")
        with self.channel_path.open() as f:
            raw_channels = json.load(f)

        self.channels = list(sorted(set(raw_channels)))
        if raw_channels != self.channels:
            with self.channel_path.open("w") as f:
                json.dump(self.channels, f, indent=2)

        super().__init__(prefix=["c!!"], irc_token=auth.irc_token,
                         nick=auth.username, initial_channels=self.channels)

    async def event_ready(self):
        print(colored("Bot ready", "green", attrs=["bold"]))
        print(colored("Username:", attrs=["bold"]), auth.username)
        print(colored("Channels:", attrs=["bold"]),
              ", ".join(self.channels))

    async def event_message(self, message):
        username = message.author.name
        if username != auth.username:
            return

        colour = self.colours[self.count]
        msg = f".color {colour}"
        try:
            await message.channel.colour(colour)
        except twitchio.errors.EchoMessageWarning:
            return

        print("{}  [{}] {}: {}".format(
            current_time(),
            colored(message.channel, attrs=["bold"]),
            colored(username, "blue", attrs=["bold"]),
            msg
        ))

        if self.count == len(self.colours) - 1:
            self.count = 0
        else:
            self.count += 1

        await self.handle_commands(message)

    @commands.command(name="join_channels")
    async def join(self, ctx, *, channels):
        await self.join_channels(channels.split())

        self.channels.extend(channels.split())
        self.channels.sort()
        with self.channel_path.open("w") as f:
            json.dump(self.channels, f, indent=2)


bot = Bot()
bot.run()
