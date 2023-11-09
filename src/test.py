import os

from dotenv import load_dotenv

load_dotenv()


xata_api_key = os.getenv("XATA_API_KEY")
xata_db_url = os.getenv("XATA_DB_URL")
