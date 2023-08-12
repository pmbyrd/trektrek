"""Summary: This file helps to define custom commands for the flask application.
"""

import os
import click
from app.extensions import db
from app import create_app
app = create_app()
# Register the custom commands with the application


def register(app):
    @app.cli.group()
    def custom_db():
        """Custom database commands."""
        pass

    @custom_db.command("create")
    def create_db():
        """Create the database."""
        db.create_all()
        print('Database created.')

    @custom_db.command("drop")
    def drop_db():
        """Drop the database."""
        db.drop_all()
        print('Database dropped.')

    @custom_db.command("print")
    def print_db():
        """Print the database."""
        print(db)

    @custom_db.command("init")
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized.')
        
    @custom_db.command("drop")
    @click.argument('table_name')  # Import 'click' for argument handling
    def drop_db(table_name):
        """Drop a specific table from the database."""
        if table_name in db.metadata.tables:
            db.engine.execute(f"DROP TABLE {table_name}")
            print(f"Table '{table_name}' dropped.")
        else:
            print(f"Table '{table_name}' not found in the database.")
            
    @app.cli.command("seed")
    def seed_db():
        """Seed the database."""
        
        db.create_all()
        from app.seeds.seed import seed_users
        seed_users()
        
        print('Database seeded.')