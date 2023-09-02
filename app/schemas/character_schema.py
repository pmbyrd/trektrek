from app.extensions import ma
from app.models.star_trek_models import Character
from flask_marshmallow.fields import URLFor, Hyperlinks

class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character
        include_fk = True