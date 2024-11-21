from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "06c23ba5a896feb881b048f56f714edc")
      API_ID = int(getenv("API_ID", "22820722"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7793548536:AAH1QMNv1IjERK28T8zeUDieldD-l3hvUYI")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002417706539:-1002314753184").replace("\n", " ").split(' '))


# Don't Remove Credit @symonads
# Subscribe YouTube Channel For Amazing Bot @symonads
# Ask Doubt on telegram @symonads
