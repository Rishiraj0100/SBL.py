from discord.ext.commands import Cog
from .client import SBLApiClient

class SBLCog(
  Cog
):
  def __init__(
    self,
    bot,
    auth: str
  ):
    self.bot = bot
    if not hasattr(
      self.bot,
      "SBLClient"
    ):
      SBLApiClient(
        self.bot,
        auth
      )
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

  @classmethod
  def setup(
    cls,
    bot,
    auth: str = ""
  ):
    cls(
      bot,
      auth
    )
