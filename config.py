from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", None)
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
DB_CHANNEL_ID = os.getenv("DB_CHANNEL_ID")
IS_PRIVATE = os.getenv("IS_PRIVATE", False)
OWNER_ID = int(os.getenv("OWNER_ID"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.getenv('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.getenv("AUTH_USERS", "").split(" ")) if os.getenv("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
