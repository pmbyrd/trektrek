"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db, login
from datetime import datetime
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin,
)


DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"

class User(db.Model, UserMixin):
    """User in the system."""

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text(32), nullable=True, unique=True)
    first_name= db.Column(db.Text(32), nullable=True)
    last_name = db.Column(db.Text(32), nullable=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    profile_pic = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pwd = db.Column(db.Text, nullable=False)
    
    @property
    # create a property that returns the full name of the user
    def full_name(self):
        """Returns a user's full name."""
        if self.first_name is None or self.last_name is None:
            return "Anonymous"
        else:
            full_name = f"{self.first_name} {self.last_name}"
            return full_name
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
     