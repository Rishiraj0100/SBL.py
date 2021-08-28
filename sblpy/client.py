from typing import Union
from discord import Client, AutoShardedClient
from discord.ext.commands import Bot, AutoShardedBot
from .http import Route
from .error import SBLError

class SBLApiClient:
  def __init__(
    self,
    bot: Union[
      Client,
      AutoShardedClient,
      Bot,
      AutoShardedBot
   ]
    auth_token: str
  ) -> None:
    self.bot = bot
    self.token = token

  @property
  def id(
    self
  ) -> int:
    return int(
      self.bot.user.id
    )

  def postBotStats(
    self
  ):
    headers = {
      "authorization": str(
        self.token
      ),
      "Content-Type": "application/json"
    }
    payload = {
      "server_count": len(
        self.bot.guilds
      )
    }
    route = Route(
      "POST",
      "/stats/{id}",
      headers = headers,
      json = payload,
      id = self.id
    )
    try:
      resp = route.go().json()
    except:
      print(
        "Ignoring exception in postBotStats, SmartBots server is offline"
      )
      return

    if str(
      resp.get(
        "success"
      )
    ).lower() == "false":
        raise SBLError(
          resp.get(
            "error"
          )
        )

    return resp

  def getBotLikes(
    self
  ):
    headers = {
      "authorization": str(self.token)
    }
    route = Route(
      "GET",
      "/liked/{id}",
      headers = headers,
      id = self.id
    )
    try:
      resp = route.go().json()
    except:
      print(
        "Ignoring exception in postBotStats, SmartBots server is offline"
      )
      return

    if str(
      resp.get(
        "success"
      )
    ).lower() == "false":
        raise SBLError(
          resp.get(
            "error"
          )
        )

    return resp
