from app.extensions import ma
from app.models.models import User, Tag
from app.models.star_trek_models import (
    Animal,
    AstronomicalObject, 
    Character,
    Element,
    Location,
    Performer,
    Movie,
    Season,
    Episode,
    Series,
    Spacecraft,
    SpacecraftClass,
    Material,
    Conflict,
    Food,
    Technology,
    Occupation,
    Species,
    Title,
    Weapon,
    )
from flask_marshmallow.fields import URLFor, Hyperlinks


# Define the Marshmallow schema for the User class

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        include_fk = True
        
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        include_fk = True

class AstronomicalObjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AstronomicalObject
        include_fk = True

class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character
        include_fk = True
        
        @staticmethod
        def dump_all_characters():
            """Dump all characters in the database"""
            characters = Character.query.all()
            character_schema = CharacterSchema(many=True)
            result = character_schema.dump(characters)
            return result
        
        

class ElementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Element
        include_fk = True

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        include_fk = True

class PerformerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Performer
        include_fk = True

class SeasonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Season
        include_fk = True

class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
        include_fk = True

class SeriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Series
        include_fk = True

class SpacecraftSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Spacecraft
        include_fk = True

class SpacecraftClassSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SpacecraftClass
        include_fk = True

class MaterialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Material
        include_fk = True

class ConflictSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Conflict
        include_fk = True

class FoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Food
        include_fk = True

class TechnologySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Technology
        include_fk = True

class OccupationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Occupation
        include_fk = True

class SpeciesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Species
        include_fk = True

class TitleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Title
        include_fk = True
        
        

class WeaponSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Weapon
        include_fk = True
        
        