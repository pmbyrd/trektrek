import os

def deploy():
	"""Run deployment tasks."""
	from app import create_app
	from app.extensions import db
	from flask_migrate import init, stamp, migrate, upgrade
	
	# migrate database to latest revision
	# handle if a migration repo already exists
	if not os.path.exists('migrations'):
		init()
	
	stamp()
	migrate()
	upgrade()

	
deploy()