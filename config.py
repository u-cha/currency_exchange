from dotenv import load_dotenv
import os

load_dotenv()

# extract DB related env variables
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_PORT = os.getenv("DB_PORT")

DB_NAME = os.getenv("DB_NAME")

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

JWT_SECRET = os.getenv("JWT_SECRET")
USER_MANAGER_SECRET = os.getenv("USER_MANAGER_SECRET")
