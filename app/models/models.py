"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from datetime import datetime
from flask_login import UserMixin
from flask import session
from app.extensions import bcrypt


DEFAULT_IMAGE_URL = "app/static/images/default-pic.png"

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
    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')
    
    # Authentication methods
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)
    
    def to_json(self):
        return {"username": self.username,
                "email": self.email}
    @property
    # create a property that returns the full name of the user
    def full_name(self):
        """Returns a user's full name."""
        if self.first_name is None or self.last_name is None:
            return "Anonymous"
        else:
            full_name = f"{self.first_name} {self.last_name}"
            return full_name
        
    # create a property to see the number of posts a user has
    def post_count(self):
        """Returns the number of posts a user has."""
        return len(self.posts)
    
        
    @property
    def get_username(self):
        """Returns a user's username."""
        if self.username is None:
            return "Anonymous"
        else:
            return self.username
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
     
    @classmethod
    def create(cls, username, first_name, last_name, email, pwd, profile_pic = DEFAULT_IMAGE_URL, bio = "", location = ""):
        """Create a new user."""
        hashed_pwd = bcrypt.generate_password_hash(pwd).decode('UTF-8')
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            profile_pic=profile_pic,
            bio=bio,
            location=location,
            joined_at=datetime.utcnow(),
            pwd=hashed_pwd
        )
        db.session.add(new_user)
    
        return new_user
    
        
    @classmethod
    def authenticate(cls, email, pwd):
        """Find a user with the given email and password."""
        user = cls.query.filter_by(email=email).first()
        
        if user:
            is_auth = bcrypt.check_password_hash(user.pwd, pwd)
            if is_auth:
                return user
        else:
            return False
        
    # create a class method that will create a user from the google auth data
    @classmethod
    def create_from_google(cls, data):
        new_user = cls(
            username=None,
            first_name=data['given_name'],
            last_name=data['family_name'],
            email=data['email'],
            profile_pic=data['picture'],
            bio=None,
            location=None,
            joined_at=datetime.utcnow(),
            pwd=None
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user    

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # A post belongs to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
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
    posts = db.relationship('Post', 
                            secondary='posts_tags',
                            backref='tags',
                            cascade='all, delete'
                            )
    
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
    
class PostTag(db.Model):
    __tablename__ = "posts_tags"
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    
    def __repr__(self):
        return f"<PostTag post_id={self.post_id}, tag_id={self.tag_id}>"
    
    @classmethod
    def create(cls, post_id, tag_id):
        new_post_tag = cls(
            post_id=post_id,
            tag_id=tag_id
        )
        db.session.add(new_post_tag)
        db.session.commit()
        return new_post_tag

