import os
import sys
from click import echo
from flask import Flask


# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login_manager, oauth, sa, ma
from config import Config
from app.helper import configure_logging, connect_db
from app.models.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    print(f"Using config class: {config_type}")
    app.config.from_object(config_type)
    db.init_app(app)
    # NOTE schemas must be initialized after db
    ma.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)
    configure_logging(app)
    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if 'users' not in inspector.get_table_names():
        with app.app_context():
            db.create_all()
            print('Database created.')
    # Register the blueprints with the application
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.universe import universe
    app.register_blueprint(universe)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()
    
    echo(f"Running the application in {app.config['FLASK_ENV']} environment.")
    echo(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    echo(f"Database engine: {engine}")
    echo(f"Database inspector: {inspector}")
    return app



