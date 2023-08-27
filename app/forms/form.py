"""File for all forms in the application"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Email, Length, Optional, URL, NumberRange, ValidationError
from email_validator import validate_email
from app.models.models import User

class UserForm(FlaskForm):
    """Form for creating a new user."""
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=64)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=64)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=64)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=1, max=64)])
    profile_pic = StringField('Profile Picture', validators=[Optional(), URL(), Length(min=1, max=500)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(min=1, max=500)])
    location = StringField('Location', validators=[Optional(), Length(min=1, max=64)])
    pwd = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=64)])
    
    def validate_username(self, username):
        """Validate that the username is unique."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')
    
    def validate_email(self, email):
        """Validate that the email is unique."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')
        
class LoginForm(FlaskForm):
    """Form for logging in a user."""
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=1, max=64)])
    pwd = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=64)])
    remember = BooleanField('Remember Me')
    
class EditUserForm(FlaskForm):
    """Allows a user to edit their profile."""
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=64)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=64)])
    profile_pic = StringField('Profile Picture', validators=[Optional(), URL(), Length(min=1, max=500)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(min=1, max=500)])
    location = StringField('Location', validators=[Optional(), Length(min=1, max=64)])
    pwd = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=64)])
    
    def validate_username(self, username):
        """Validate that the username is unique."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')
    
    def validate_email(self, email):
        """Validate that the email is unique."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')    