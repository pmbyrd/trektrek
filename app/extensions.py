"""File to keep track of extensions used in the app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############HELPER FUNCTIONS############
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)