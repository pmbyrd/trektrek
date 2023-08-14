import os
import sys
import sqlalchemy as sa
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
from click import echo
from flask import Flask


# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login_manager, oauth
from config import Config
from app.models.models import User

def create_app(config_filename=None):
    app = Flask(__name__)
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    db.init_app(app)
    # NOTE schemas must be initialized after db
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)
    configure_logging(app)
    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table("users"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info('Initialized the database!')
    else:
        app.logger.info('Database already contains the users table.')
   
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.universe import universe
    app.register_blueprint(universe)
    print(app.config)
    return app


def configure_logging(app):
    # Logging Configuration
    if app.config['LOG_WITH_GUNICORN']:
        gunicorn_error_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    # else:
    #     file_handler = RotatingFileHandler('instance/trektrek.log',
    #                                        maxBytes=16384,
    #                                        backupCount=20)
    #     file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
    #     file_handler.setFormatter(file_formatter)
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask User Management App...')
