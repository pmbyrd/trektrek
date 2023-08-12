import os
import sys
from flask import Flask


# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login_manager, oauth
from config import Config
from app.models.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    SQLALCHEMY_DATABASE_URI = "postgresql:///trektrek"
    db.init_app(app)
    # NOTE schemas must be initialized after db
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import auth
    app.register_blueprint(auth)
    
    return app