import os
from dotenv import load_dotenv
load_dotenv(override=True)

APP_VERSION = os.getenv("APP_VERSION")
MONGO_URI = os.getenv("MONGO_URI")