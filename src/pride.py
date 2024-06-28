from twitchio.ext import commands


class BotPride(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pride")
    async def cmd_pride(self, ctx: commands.Context):
        await ctx.send("❤️❤️❤️❤️❤️❤️")
        await ctx.send("💛💛💛💛💛💛")
        await ctx.send("💚💚💚💚💚💚")
        await ctx.send("💙💙💙💙💙💙")
        await ctx.send("💜💜💜💜💜💜")

    @commands.command(name="lesbian")
    async def cmd_lesbian(self, ctx: commands.Context):
        await ctx.send("🧡🧡🧡🧡🧡🧡")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("🩷🩷🩷🩷🩷🩷")

    @commands.command(name="bi")
    async def cmd_bi(self, ctx: commands.Context):
        await ctx.send("❤️❤️❤️❤️❤️❤️")
        await ctx.send("💜💜💜💜💜💜")
        await ctx.send("💙💙💙💙💙💙")

    @commands.command(name="pan")
    async def cmd_pan(self, ctx: commands.Context):
        await ctx.send("🩷🩷🩷🩷🩷🩷")
        await ctx.send("💛💛💛💛💛💛")
        await ctx.send("💙💙💙💙💙💙")

    @commands.command(name="trans")
    async def cmd_trans(self, ctx: commands.Context):
        await ctx.send("💙💙💙💙💙💙")
        await ctx.send("🩷🩷🩷🩷🩷🩷")
        await ctx.send("🤍🤍🤍🤍🤍🤍")

    @commands.command(name="nb")
    async def cmd_nb(self, ctx: commands.Context):
        await ctx.send("💛💛💛💛💛💛")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("💜💜💜💜💜💜")
        await ctx.send("🖤🖤🖤🖤🖤🖤")

    @commands.command(name="agender")
    async def cmd_agender(self, ctx: commands.Context):
        await ctx.send("🖤🖤🖤🖤🖤🖤")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("💚💚💚💚💚💚")

    @commands.command(name="genderqueer")
    async def cmd_genderqueer(self, ctx: commands.Context):
        await ctx.send("💜💜💜💜💜💜")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("💚💚💚💚💚💚")

    @commands.command(name="ace")
    async def cmd_ace(self, ctx: commands.Context):
        await ctx.send("🖤🖤🖤🖤🖤🖤")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("💜💜💜💜💜💜")

    @commands.command(name="aro")
    async def cmd_aro(self, ctx: commands.Context):
        await ctx.send("💚💚💚💚💚💚")
        await ctx.send("🤍🤍🤍🤍🤍🤍")
        await ctx.send("🖤🖤🖤🖤🖤🖤")

    @commands.command(name="demi")
    async def cmd_demi(self, ctx: commands.Context):
        await ctx.send("🖤🤍🤍🤍🤍🤍")
        await ctx.send("🖤🖤🤍🤍🤍🤍")
        await ctx.send("🖤🖤🖤💜💜💜")
        await ctx.send("🖤🖤🤍🤍🤍🤍")
        await ctx.send("🖤🤍🤍🤍🤍🤍")


def setup(bot):
    bot.add_cog(BotPride(bot))
