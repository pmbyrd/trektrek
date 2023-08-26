from app.extensions import ma
from app.models.models import User
from flask_marshmallow.fields import URLFor, Hyperlinks

# Define the Marshmallow schema for the User class
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        
    