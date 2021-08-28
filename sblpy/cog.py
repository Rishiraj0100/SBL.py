from discord.ext.commands import Cog

class SBLCog(
  Cog
):
  def __init__(
    self,
    bot
  ):
    self.bot = bot
    self.bot.add_cog(
      self
    )

  @Cog.listener()
  async def on_guild_join(
    self
  ):
    self.bot.SBLClient.postBotStats()

  @Cog.listener()
  async def on_guild_remove(
    self
  ):
    self.bot.SBLClient.postBotStats()


def setup(
  bot
):
  SBLCog(
    bot
  )
