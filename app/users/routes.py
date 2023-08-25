"""Summary this page contains the routes for the users blueprint."""
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.users import users
from app.extensions import db
from app.models.models import User, Post, Tag, PostTag
from app.helpers import MemoryAlphaScraper, replace_space

# Start with the post routes for now since at the moment they do not require a user to be logged in.
@users.route('/posts')
def posts():
    """This page series all the posts in the database."""
    posts = Post.query.all()
    
    return render_template('posts/posts.html', posts=posts, title="Posts")