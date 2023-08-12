from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
oauth = OAuth()