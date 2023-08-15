import cli
import os
from app import create_app
from app.extensions import db
from app.models.models import User
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
    Weapon
    )

app = create_app()
app.app_context().push()
# Register the custom commands with the application
cli.register(app)
# Check if the environment is "development" or "production"
port = int(os.environ.get("PORT", 5000))
host = os.environ.get("HOST", "0.0.0.0")



# make sure the database is created
# use the click command to create the database instance for the application for deployment
@app.cli.command("create")

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
    }
if __name__ == '__main__':
    app.run(host=host, port=port)
    print(os.environ.get("FLASK_ENV"))
    print('Running the application!')