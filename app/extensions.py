"""File to keep track of extensions used in the app."""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

############HELPER FUNCTIONS############
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)