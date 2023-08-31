from app.extensions import ma
from app.models.models import Tag
from flask_marshmallow.fields import URLFor, Hyperlinks

# Define the Marshmallow schema for the Tag class
class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        include_fk = True
        