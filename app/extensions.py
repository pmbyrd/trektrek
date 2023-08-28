import sqlalchemy

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from authlib.integrations.flask_client import OAuth
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
oauth = OAuth()
ma = Marshmallow()
sa = sqlalchemy
CORS = CORS()
bcrypt = Bcrypt()
