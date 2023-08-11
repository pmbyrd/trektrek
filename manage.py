def deploy():
	"""Run deployment tasks."""
	from app import create_app
	from app.extensions import db
	from flask_migrate import init, stamp, migrate, upgrade

	app = create_app()
	app.app_context().push()
	db.create_all()

	# migrate database to latest revision
	init()
	stamp()
	migrate()
	upgrade()
	
deploy()