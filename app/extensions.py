from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_login import Login
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
migrate = Migrate()
login = Login()
seeder = FlaskSeeder()
oauth = OAuth()