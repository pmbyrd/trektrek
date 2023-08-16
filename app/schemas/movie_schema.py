from app.extensions import ma
from app.models.star_trek_models import Movie
from flask_marshmallow.fields import URLFor, Hyperlinks

# Define the Marshmallow schema for the Movie class
class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        include_fk = True
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()
