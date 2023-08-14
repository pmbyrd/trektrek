import os
from dotenv import load_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
db_username = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')

class Config:
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    elif os.getenv('DATABASE_URL') is None:
        SQLALCHEMY_DATABASE_URI = f"postgresql://{db_username}:{db_password}@localhost/trektrek"    
    else:
        f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
