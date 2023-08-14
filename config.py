import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'postgresql:///trektrek')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI', 'postgresql:///trektrek_prod').replace("postgres://", "postgresql://", 1)

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # Add more configurations if needed
}

load_dotenv()

# Select the appropriate configuration based on the FLASK_ENV environment variable
config = config_by_name.get(os.getenv('FLASK_ENV', 'development'))


