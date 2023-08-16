import os
import sys
from flask import Flask


# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, login_manager, oauth, sa
from config import Config
from app.helper import configure_logging
from app.models.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config['SQLALCHEMY_BINDS'] = {
    #     'users': f"postgresql://{app.config['SQLALCHEMY_DATABASE_URI']}/users"
    # }   

    
    db.init_app(app)
    # NOTE schemas must be initialized after db
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)
    # configure_logging(app)
    # engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    # inspector = sa.inspect(engine)
    # if 'users' not in inspector.get_table_names():
    #     with app.app_context():
    #         db.create_all()
        
    
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

    # print(app.config)
    # print("app created")
    # print(os.environ.get("FLASK_ENV"))
    # print('Running the application!')
    return app