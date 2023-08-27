"""Summary this page contains the routes for the users blueprint."""
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.users import users
from app.extensions import db
from app.models.models import User, Post, Tag, PostTag, DEFAULT_IMAGE_URL
from app.helpers import MemoryAlphaScraper, replace_space
from random import randint
from app.schemas.user_schema import UserSchema
from sqlalchemy import desc
from app.forms.form import UserForm
from sqlalchemy.exc import IntegrityError


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

# Make a route to create a new user and add it to the database
@users.route('/new', methods=['GET', 'POST'])
def create_user():
    """Handles form submission for creating a new user."""
    form = UserForm(request.form)
    if form.validate_on_submit():
        try:
            new_user = User.create(
                username=form.username.data,
                first_name=form.first_name.data, 
                last_name=form.last_name.data,
                email=form.email.data,
                profile_pic=form.profile_pic.data or DEFAULT_IMAGE_URL,
                bio=form.bio.data or None,
                location=form.location.data or None,
                pwd=form.pwd.data
            )
            flash(f"User {new_user.full_name} added.")
            # if the user has been successfully added to the database, authenticate the user and log them in using the login_user() function
            
            db.session.commit()
            login_user(new_user)    
            return redirect(url_for('users.user_profile', user_id=new_user.id))
        except IntegrityError:
            flash("Username or email already exists.")
            return render_template('users/new_user.html', form=form, title="New User")
    return render_template('users/new_user.html', form=form, title="New User")


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