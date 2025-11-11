import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SWAGGER = {
        'title': 'Blog API',
        'uiversion': 3
    }