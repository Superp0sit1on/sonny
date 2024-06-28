from twitchio.ext import commands


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # General Commands

    @commands.command(name="bttv")
    async def cmd_bttv(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name}:")
        await ctx.send(
            "BabyYodaSip catJAM Clap CuteDog KEKW KirbDance KlonoaPat kumaPls NOTED peepoRain pepeD PETTHEMODS ppJedi pressF somDied ThisIsFine"
        )

    @commands.command(name="love")
    async def cmd_love(self, ctx: commands.Context):
        await ctx.send("❤️❤️❤️❤️❤️❤️")
        await ctx.send("❤️❤️❤️❤️❤️❤️")
        await ctx.send("❤️❤️❤️❤️❤️❤️")

    @commands.command(name="links")
    async def cmd_links(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name}:")
        await ctx.send("🤍 Website: https://juliomartins.dev")
        await ctx.send("🖤 GitHub: https://github.com/superp0sit1on")
        await ctx.send("❤️ YouTube: https://www.youtube.com/@superp0sit1on")
        await ctx.send("💜 Discord: thinking about it...")

    @commands.command(name="specs")
    async def cmd_specs(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name}, here are our current specs:")
        await ctx.send("💻 Thinkpad x240:")
        await ctx.send("- OS: Windows 11 Pro")
        await ctx.send("- CPU: Intel Core i5-4300U")
        await ctx.send("- RAM: 2x4GB 1600")
        await ctx.send("- Storage #1: 128GB SSD")
        await ctx.send("- Storage #2: 600GB HDD")
        await ctx.send("🎧 CCA CRA Headphone")
        await ctx.send("🎮 Nintendo Switch Pro Controller - Zelda Tears of the Kingdom")
        await ctx.send("🖱️ SEENDA Ergonomic Wireless Mouse")

    # EN-US Commands

    @commands.command(name="about")
    async def cmd_about(self, ctx: commands.Context):
        await ctx.send(
            f"{ctx.author.name} Júlio (he/they), or just Ju, is a non-binary person and Software Engineer (previously IBM), based in São Paulo, Brazil."
        )
        await ctx.send("Type !channel for more info...")

    @commands.command(name="bye")
    async def cmd_bye(self, ctx: commands.Context):
        await ctx.send(f"tks for coming {ctx.author.name}! 👋")

    @commands.command(name="channel")
    async def cmd_channel(self, ctx: commands.Context):
        await ctx.send(
            f"{ctx.author.name} we mostly chit-chat and play games over here, specially retro ones, but we also talk about technology and develop some projects sometimes."
        )
        await ctx.send(
            "🙋‍♂️ Although the main language of the channel is Brazilian Portuguese, feel free to chat with us in English if you're not from Portuguese speaking countries."
        )

    @commands.command(name="rules")
    async def cmd_rules(self, ctx: commands.Context):
        await ctx.send("1. Basically, respect everyone and they pronouns!")
        await ctx.send(
            "2. Avoid talking about sensitive topics, we're trying to make this channel a chill place."
        )
        await ctx.send(
            "3. Please, dot not promote anything or anyone without permission."
        )
        await ctx.send(
            "4. For security reasons, with rare exceptions, only subs, friends and long-stayed viewers can play with us on stream, so please, don't ask or insist to join."
        )
        await ctx.send(
            "☝🤓 Our mod are free to give a timeout or just ban someone who break any of our rules without warning!"
        )

    @commands.command(name="support")
    async def cmd_donate(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name}, you can support the channel:")
        await ctx.send("💳 Subscribing directly")
        await ctx.send("👑 Subscribing with Prime Gaming")
        await ctx.send("🎁 Gifting subscriptions")
        await ctx.send("🪙 Sending bits")

    # PT-BR Commands

    @commands.command(name="apoio")
    async def cmd_apoio(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name}, você pode apoiar o canal:")
        await ctx.send("💳 Se inscrevendo normalmente")
        await ctx.send("👑 Se inscrevendo com Prime Gaming")
        await ctx.send("🎁 Presenteando inscrições")
        await ctx.send("🪙 Enviando bits")

    @commands.command(name="tchau")
    async def cmd_tchau(self, ctx: commands.Context):
        await ctx.send(f"obrigade por vir {ctx.author.name}! 👋")

    @commands.command(name="canal")
    async def cmd_canal(self, ctx: commands.Context):
        await ctx.send(
            f"{ctx.author.name} por aqui costumamos mais papear e jogar alguns jogos despretensiosamente, especialmente retros, mas também falamos sobre tecnologia e desenvolvemos alguns projetos de vez em quando."
        )

    @commands.command(name="rules")
    async def cmd_rules(self, ctx: commands.Context):
        await ctx.send("1. Basicamente, respeite todo mundo e seus pronomes!")
        await ctx.send(
            "2. Evite falar sobre tópicos sensíveis, nós estamos tentando manter esse canal um espaço tranquilo."
        )
        await ctx.send("3. Por favor, não divulgue nada nem ninguém sem permissão.")
        await ctx.send(
            "4. Por questões de segurança, com raras exceções, apenas subs, amizades e pessoas que acompanhem a canal um bom tempo poderão jogar em live conosco, então por favor, não peça ou insista para entrar."
        )
        await ctx.send(
            "☝🤓 As pessoas mods do canal estão livres para dar timeout ou banir qualquer pessoa que quebrar qualquer uma das regras sem aviso!"
        )

    @commands.command(name="sobre")
    async def cmd_sobre(self, ctx: commands.Context):
        await ctx.send(
            f"{ctx.author.name} Júlio (ele/delu), ou só Ju, é uma pessoa não-binária e desenvolvedora (ex-IBM), de São Paulo, capital."
        )
        await ctx.send("Digite !canal para mais informações...")


def setup(bot):
    bot.add_cog(BotCommands(bot))
