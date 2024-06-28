from colorama import Fore
from twitchio.ext import commands

from commands import setup as commands_setup
from config import CHANNELS, NICKNAME, TOKEN
from greetings import Greetings
from pride import setup as pride_setup


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TOKEN, nick=NICKNAME, prefix="!", initial_channels=CHANNELS
        )
        commands_setup(self)
        pride_setup(self)
        self.greetings = Greetings()

    async def event_ready(self):
        print(Fore.MAGENTA + f"🎉 | Successfully connected as @{self.nick} on Twitch!")

    async def event_message(self, message):
        datetime = message.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        if message.echo:
            print(Fore.BLUE + f"🤖 | {datetime} | @{self.nick}: {message.content}.")
        else:
            print(
                Fore.GREEN
                + f"💬 | {datetime} | @{message.author.name}: {message.content}."
            )
            await self.greetings.handle_greeting(message)
            await self.handle_commands(message)

    async def event_command_error(error):
        print(Fore.RED + "⚠️ " + error)

    @commands.command(name="cmd")
    async def cmd_list(self, ctx: commands.Context):
        commands = list(self.commands.keys())
        await ctx.send(f'{ctx.author.name}: !{", !".join(commands)}.')


bot = Bot()
bot.run()
