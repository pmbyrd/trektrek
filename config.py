import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'postgresql:///trektrek'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql:///trektrek')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # or 'sqlite:///' + os.path.join(basedir, 'app.db') or 