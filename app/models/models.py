"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
from flask import session


DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"

class User(db.Model, UserMixin):
    """User in the system."""

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=True, unique=True)
    first_name= db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    profile_pic = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pwd = db.Column(db.Text, nullable=True)
    
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
     
    @classmethod
    def create(cls, sub, name, email, picture):
        """
        Create a new User instance based on Google authentication data.
        
        :param sub: Subject identifier from Google response (sub field).
        :param name: User's name from Google response (name field).
        :param email: User's email from Google response (email field).
        :param picture: User's profile picture URL from Google response (picture field).
        :return: New User instance.
        """
        new_user = cls(
            username=None,  # You might set this based on your app's logic
            first_name=None,  # You might set this based on your app's logic
            last_name=None,  # You might set this based on your app's logic
            email=email,
            profile_pic=picture,
            bio=None,  # You might set this based on your app's logic
            location=None,  # You might set this based on your app's logic
            joined_at=datetime.utcnow(),
            pwd=None,  # You might set this based on your app's logic
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @classmethod
    def authenticate_session_user(cls, user):
        if 'user' in session:
            new_user = cls(
                email = user['email']
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user
        
    @classmethod
    def authenticate(cls, email, pwd):
        """Find a user with the given email and password."""
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        else:
            return False
        
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # should refrence also the users table
    user = db.relationship('User', backref='posts')
    def __repr__(self):
        return f"<Post #{self.id}: {self.title}, {self.created_at}>"
    
    @classmethod
    def create(cls, title, body, user_id):
        new_post = cls(
            title=title,
            body=body,
            user_id=user_id
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
class Tag(db.Model):
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Tag #{self.id}: {self.name}>"
    
    @classmethod
    def create(cls, name):
        new_tag = cls(
            name=name
        )
        db.session.add(new_tag)
        db.session.commit()
        return new_tag