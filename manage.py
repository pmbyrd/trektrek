import os

def deploy(host, port):
	"""Run deployment tasks."""
	from app import create_app
	from app.extensions import db
	from flask_migrate import init, stamp, migrate, upgrade
	app = create_app()
	app.app_context().push()
	
	if not os.path.exists('migrations'):
		init()
	stamp()
	migrate()
	upgrade()
	db.create_all()

	
deploy(host='0.0.0.0', port=10000)