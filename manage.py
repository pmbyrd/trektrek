from flask import Flask
import os
from app import create_app
# from app.helpers import get_random_datetime, test_hello
app = create_app()

def deploy():
    """Run deployment tasks."""
    from app.extensions import db
    from flask_migrate import upgrade, init, migrate, stamp
    
    app.app_context().push()
    db.create_all()
    # db.init_app(app)
    
    #migrate database to latest revision
    if os.path.exists('migrations') is None:
        init()
        stamp()
        migrate()
        upgrade()
        print('Database initialized.')
    else:
        stamp()
        migrate()
        upgrade()
        print('Database upgraded to latest revision.')
    print('Application deployed.')