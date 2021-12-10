import os
from dotenv import load_dotenv

#? load Environment Variables from .env file
load_dotenv()


class Config(object):
    '''
        Gather Environment Variables for app
    '''
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
