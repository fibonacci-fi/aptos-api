import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
