"""Summary this page contains the routes for the users blueprint."""
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.users import users
from app.extensions import db
from app.models.models import User, Post, Tag, PostTag, DEFAULT_IMAGE_URL
from app.helpers import MemoryAlphaScraper, replace_space
from random import randint, sample
from app.schemas.schemas import UserSchema, TagSchema
from sqlalchemy import desc, func
from app.forms.form import UserForm, LoginForm, EditUserForm, DeleteAccountForm, PostForm
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
@users.route('/<int:user_id>')
def user_profile(user_id):
    """This page displays a user's profile."""
    user = User.query.get_or_404(user_id)
    
    return render_template('users/user_profile.html', user=user, title="User Profile")

@users.route('/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    """This page allows a user to edit their profile."""
    user = User.query.get_or_404(user_id)
    form = EditUserForm(obj=user)
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.profile_pic = form.profile_pic.data
        user.bio = form.bio.data
        user.location = form.location.data
        user.pwd = form.pwd.data
        if current_user.is_authenticated:
            db.session.add(user)
            db.session.commit()
            print(user.profile_pic)
            flash("User profile updated.")
            return redirect(url_for('users.user_profile', user_id=user.id))
    return render_template('users/edit.html', user=user, form=form, title="Edit User")

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
            # if the user has been successfully added to the database, authenticate the user and log them in using the login_user() function
            db.session.commit()
            login_user(new_user)    
            flash(f"User {new_user.full_name} added.")
            return redirect(url_for('users.user_profile', user_id=new_user.id))
        except IntegrityError:
            flash("Username or email already exists.")
            return render_template('users/new_user.html', form=form, title="New User")
    return render_template('users/new_user.html', form=form, title="New User")

@users.route('/login', methods=['GET', 'POST'])
def user_login():
    """Login a user."""
    if current_user.is_authenticated:
        return redirect(url_for('users.user_profile', user_id=current_user.id))
    # import pdb; pdb.set_trace()
    form = LoginForm(request.form)
    if form.validate_on_submit():
        try:
            user = User.authenticate(form.email.data,
                                     form.pwd.data)
            # import pdb; pdb.set_trace()
            print(user)
            if user:
                login_user(user, remember=form.remember.data)
                flash(f"Welcome back, {user.full_name}!")
                print(user)
                return redirect(url_for('users.user_profile', user_id=user.id))
        except IntegrityError:
            flash("Invalid email or password.")
            return render_template('users/login.html', form=form, title="Login")
    print("last line in login route")
    return render_template('users/login.html', form=form, title="Login")

@users.route('/logout')
@login_required
def user_logout():
    """Logout a user."""
    logout_user()
    return redirect(url_for('main.index'))

@users.route('/user_info', methods=['GET'])
def user_info():
    if current_user.is_authenticated:
        resp = {"result": 200,
                "data": current_user.to_json()}
    else:
        resp = {"result": 401,
                "data": {"message": "user no login"}}
    return jsonify(**resp)

# Note make the ability to delete a user account
@users.route('/<int:user_id>/delete', methods=['GET','POST'])
@login_required
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    # if a user wants to delete their account this can not be undone
    form = DeleteAccountForm(obj=user)
    if form.validate_on_submit():
        try:
            if user.username == form.username.data and user.pwd == form.pwd.data:
                db.session.delete(user)
                db.session.commit()
                flash("User deleted.")
                return redirect(url_for('main.index'))
        except IntegrityError:
            flash("Incorrect username or password.")
            return render_template('users/delete.html', user=user, form=form, title="Delete User")
    return redirect(url_for('main.index'))


# *********** Post Routes ***********
@users.route('/posts')
def posts():
    """This page lists all the posts in the database."""
    tagged_posts = Post.query.filter(Post.tags.any()).all()
    # Generate 25 random post IDs within the range of available tagged post IDs
    random_tagged_post_ids = [post.id for post in tagged_posts]
    random_post_ids = sample(random_tagged_post_ids, min(len(random_tagged_post_ids), 25))
    # Query the database for the random tagged posts using the generated IDs
    random_posts = Post.query.filter(Post.id.in_(random_post_ids)).all()
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
    print([post.tags for post in random_posts])
    tags = Tag.query.all()
    ordered_tags = sorted(tags, key=lambda tag: len(tag.posts), reverse=True)
    # order the tags by the number of posts they are associated with

    return render_template('posts/posts.html', posts=formatted_posts, title="Posts", tags=ordered_tags)

@users.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    """This page allows a user to create a post."""
    form = PostForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]
    try:
        tags = Tag.query.all()
        tags = [tag.name for tag in tags]
        if form.validate_on_submit():
            new_post = Post.create(
                title=form.title.data,
                body=form.content.data,
                user_id=current_user.id
            )
            # import pdb; pdb.set_trace()
            db.session.add(new_post)
            db.session.commit()
            flash("Post created.")
            return redirect(url_for('users.posts', post_id=new_post.id))
    except IntegrityError:
        flash("Post title already exists.")
        return render_template('posts/new_post.html', form=form, title="Create Post")
    return render_template('posts/new_post.html', form=form, title="Create Post")

@users.route('/posts/<int:post_id>')
def post(post_id):
    """This page displays a post."""
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', post=post, title="Post")

@users.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]
    try:
        if form.validate_on_submit():
            post.title = form.title.data
            post.body = form.content.data
            tag_ids = [int(num) for num in request.form.getlist("tags")]
            post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
            
                
            db.session.add(post)
            db.session.commit()
            flash("Post updated.")
            return redirect(url_for('users.post', post_id=post.id))
    except IntegrityError:
        flash("Tag already exists.")
        return render_template('posts/edit_post.html', form=form, title="Edit Post")
    return render_template('posts/edit_post.html', form=form, title="Edit Post")

@users.route('/posts/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    """Allows a user to delete a post."""
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.")
        return redirect(url_for('users.user_profile', user_id=current_user.id))
    else:
        flash("You can only delete your own posts.")
        return redirect(url_for('users.posts'))

#************** Tag Routes **************


@users.route('/tags/create', methods=['GET', 'POST'])
def create_tag():
    pass

@users.route('/tags/<int:tag_id>')
def tag(tag_id):
    """Get a specific tag by id."""
    tag = Tag.query.get_or_404(tag_id)
    # Show all posts associated with a tag
    
    return render_template('tags/tag.html', tag=tag, title="Tag")

@users.route('/tags/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    pass