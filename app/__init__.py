import os
import sys
from click import echo
from flask import Flask


# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login_manager, oauth, sa, ma
from config import Config
from app.helper import configure_logging
from app.models.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # app.config['SQLALCHEMY_BINDS'] = {
    #     'users': f"postgresql://{app.config['SQLALCHEMY_DATABASE_URI']}/users"
    # }   
    port = int(os.environ.get("PORT", 10000))
    host = os.environ.get("HOST", "0.0.0.0")

    
    db.init_app(app)
    # NOTE schemas must be initialized after db
    ma.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)
    configure_logging(app)
    register_cli_commands(app)
    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if 'users' not in inspector.get_table_names():
        with app.app_context():
            db.create_all()
            print('Database created.')

    
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.universe import universe
    app.register_blueprint(universe)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()
    
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo('Initialized the database!')


    # print(app.config)
    # print("app created")
    echo(f"Running the application in {app.config['FLASK_ENV']} environment.")
    # print('Running the application!')
    return app

def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo('Initialized the database!')
