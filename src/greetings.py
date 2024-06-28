from twitchio.ext import commands

from config import BOTS
from suppress import Suppress


class Greetings:
    def __init__(self):
        self.greetings = Suppress("greetings.tmp")

    async def handle_greeting(self, ctx: commands.Context):
        name = ctx.author.name
        if name not in BOTS and self.greetings.add(name):
            await ctx.channel.send(f"{name} hello! 👋")
