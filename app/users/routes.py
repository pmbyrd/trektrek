"""Summary this page contains the routes for the users blueprint."""
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.users import users
from app.extensions import db
from app.models.models import User, Post, Tag, PostTag
from app.helpers import MemoryAlphaScraper, replace_space
from random import randint
from app.schemas.user_schema import UserSchema
from sqlalchemy import desc

#****USER ROUTES****#
# user flask login manager helper function
@users.route('/users')
def users_index():
    """This page lists all the users in the database."""
    page = request.args.get('page', 1, type=int)
    ordered_users = User.query.join(User.posts).group_by(User).order_by(desc(db.func.count(User.posts)))
    # Paginate the ordered_users
    paginated_users = ordered_users.paginate(page=page, per_page=100)
    return render_template('users/users.html', users=paginated_users, title="Users")
# when clicking on a user profile, it will take you to the user profile page
@users.route('/users/<int:user_id>')
def user_profile(user_id):
    """This page displays a user's profile."""
    user = User.query.get_or_404(user_id)
    return render_template('users/user_profile.html', user=user, title="User Profile")

@users.route('/')

# Start with the post routes for now since at the moment they do not require a user to be logged in.
@users.route('/posts')
def posts():
    """This page lists all the posts in the database."""
    posts_count = Post.query.count()
    print(posts_count)

    # Generate 25 random post IDs within the range of available IDs
    random_post_ids = [randint(1, posts_count) for _ in range(25)]
    print(random_post_ids)

    # Query the database for the random posts using the generated IDs
    random_posts = Post.query.filter(Post.id.in_(random_post_ids)).all()

    # Convert the random_posts to a format of your choice (e.g., JSON)
    formatted_posts = [
        {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            # Add more fields as needed
            'tags': [tag.name for tag in post.tags] 
        }
        for post in random_posts
    ]
    return render_template('posts/posts.html', posts=formatted_posts, title="Posts")