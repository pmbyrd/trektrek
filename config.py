import os
from dotenv import load_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
db_username = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')

# class Config:
#     if os.getenv('DATABASE_URL'):
#         SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
#     elif os.getenv('DATABASE_URL') is None:
#         SQLALCHEMY_DATABASE_URI = f"postgresql://{db_username}:{db_password}@localhost/trektrek"    
#     else:


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
    # update the URI to the postgres database to use the supported 'postgresql://' scheme
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    # else:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
