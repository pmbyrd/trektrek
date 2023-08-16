"""Summary: This file helps to define custom commands for the flask application.
"""

import os
import click
from click import echo
from app.extensions import db
# Register the custom commands with the application


def register(app):
    @app.cli.group()
    def custom_db():
        """Custom database commands."""
        pass

    @app.cli.command("create")
    def create_db():
        """Create the database."""
        db.create_all()
        print('Database created.')

    @app.cli.command("drop")
    def drop_db():
        """Drop the database."""
        db.drop_all()
        print('Database dropped.')

    @app.cli.command("print")
    def print_db():
        """Print the database."""
        print(db)

    @app.cli.command("init")
    def init_db():
        """Initialize the database."""
        click.echo("Initializing the database.")
        db.create_all()
        click.echo("Database initialized.")
            
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        echo('Initialized the database!')
        
    @app.cli.command("drop")
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

        # run the whole seed file
        from app.seeds.seed import seed_all
        try:
            seed_all()
        except Exception as e:
            if os.environ.get("FLASK_ENV") == "production":
                print("Error in seeding the database.")
                print(e)
            else:
                print(e)
                