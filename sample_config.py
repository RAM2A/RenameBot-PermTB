import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", "24665357"))
    API_HASH = os.environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1717511106").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://subham94mii2:7wRYh7ylrGEsFGkP@busybot.oskm6vj.mongodb.net/?retryWrites=true&w=majority&appName=busybot")

