def deploy():
    """Run deployment task."""
    from app import create_app
    from flask_migrate import upgrade, migrate, init, stamp
    
    app = create_app()