import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/chat_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
