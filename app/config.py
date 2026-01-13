import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

API_TOKEN = os.getenv("DOCUMENT360_API_TOKEN")
USER_ID = os.getenv("DOCUMENT360_USER_ID")

if not API_TOKEN:
    raise RuntimeError("DOCUMENT360_API_TOKEN is missing in .env")

if not USER_ID:
    raise RuntimeError("DOCUMENT360_USER_ID is missing in .env")
