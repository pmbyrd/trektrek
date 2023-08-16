import os
from app import create_app

app = create_app()

def deploy():
	"""Run deployment tasks."""
	from app.extensions import db
	from app.helper import connect_db
	from flask_migrate import init, stamp, migrate, upgrade
 
	if not os.path.exists('migrations'):
		init()
	stamp()
	migrate()
	upgrade()
	# connect_db(app)

	

if __name__ == '__main__':
    deploy()
    # create an instance of the flask application first and then run it
    # initialize the database
    app.run(host='0.0.0.0', port=10000)
    app.cli.invoke(args=['print'])
    app.cli.invoke(args=['init'])