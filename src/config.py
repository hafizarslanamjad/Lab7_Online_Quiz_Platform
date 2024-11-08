# src/config.py
import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.getcwd(), 'quiz_app.db'
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
