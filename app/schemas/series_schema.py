# import
from app.extensions import ma
from app.models.star_trek_models import Series
from flask_marshmallow.fields import URLFor, Hyperlinks

# Define the Marshmallow schema for the Series class
class SeriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Series
        include_fk = True
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()
