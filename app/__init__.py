import os
import sys
from flask import Flask

# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login, oauth, seeder
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    # NOTE schemas must be initialized after db
    migrate.init_app(app, db)
    login.init_app(app)
    oauth.init_app(app)
    seeder.init_app(app, db)
    
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app