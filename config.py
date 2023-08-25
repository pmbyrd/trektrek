import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
    # update the URI to the postgres database to use the supported 'postgresql://' scheme]
    # if the os 
    if os.getenv('DATABASE_URI'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI').replace("postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)
    


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    
class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/trektrek"
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
