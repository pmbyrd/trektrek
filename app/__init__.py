from flask import Flask
import sys
import os
from app.extensions import db, connect_db
from config import Config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    with app.app_context():
        # NOTE when loading the extensions for ma itm must come after the db extension
        connect_db(app)
        
    @app.route('/')
    def hello():
        return 'Hello World!'