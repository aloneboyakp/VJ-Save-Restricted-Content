import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23057273"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f50521c066ea8d7398e873d339652c61")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6004837126"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Akp:akpbot12345@cluster.7gupcus.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
