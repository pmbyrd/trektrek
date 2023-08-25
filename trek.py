from app import create_app
import cli
import os
from app.extensions import db
from app.models.models import User, Post, Tag, PostTag
from app.models.star_trek_models import (
    Animal,
    AstronomicalObject, 
    Character,
    Element,
    Location,
    Performer,
    Season,
    Episode,
    Series,
    Spacecraft,
    SpacecraftClass,
    Staff,
    Material,
    Conflict,
    Food,
    Technology,
    Company,
    Occupation,
    Species,
    Title,
    Weapon,
    Show, 
    )

app = create_app()
cli.register(app)
app.app_context().push()
app.logger.info("Database tables created")


# Register the custom commands with the application
# Check if the environment is "development" or "production"
if os.environ.get("FLASK_ENV") == "production":
    print("Creating the database instance for the application.")
    db.create_all()
    print("Database instance created.")
    


@app.cli.command('print')

@app.shell_context_processor
def make_shell_context():
    """Makes a shell context that adds the database instance and models to the shell session."""
    return {
        'db': db,
        'AstronomicalObject': AstronomicalObject,
        'Animal': Animal,
        'Character': Character,
        'Element': Element,
        'Location': Location,
        'Performer': Performer,
        'Season': Season,
        'Episode': Episode,
        'Series': Series,
        'Spacecraft': Spacecraft,
        'SpacecraftClass': SpacecraftClass,
        'Staff': Staff,
        'Material': Material,
        'Conflict': Conflict,
        'Food': Food,
        'Technology': Technology,
        'Company': Company,
        'Occupation': Occupation,
        'Species': Species,
        'Title': Title,
        'Weapon': Weapon,
        'User': User,
        'Show': Show,
        'Post': Post,
        'Tag': Tag,
        'PostTag': PostTag,
    }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    # create the database if it doesn't exist
    print(os.environ.get("FLASK_ENV"))
    print('Running the application!')