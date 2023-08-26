import os
from flask import render_template, abort, session, redirect, url_for
from authlib.common.security import generate_token
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.extensions import oauth, login_manager, db
from app.auth import auth
from app.models.models import User

# # flask login manager helper function
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)



@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout', methods=['GET', 'POST'])
# @login_required
def logout():
    
        # logout_user()
        # session.clear()
        # return redirect(url_for('main.index'))
    return render_template('logout.html')

@auth.route('/google/')
def google():
    # import the google client id and secret from the environment variables
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', None)
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', None)

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('auth.google_auth', _external=True)
    print(redirect_uri)
    session['nonce'] = generate_token()
    # import pdb; pdb.set_trace()
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

#FIXME - this is not working 304 error when attempting to login with google 
#NOTE - Something in relation to the redirect_uri and token and that the google client can not be found.
@auth.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    # user = oauth.google.parse_id_token(token)
    google_user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = google_user
    # import pdb; pdb.set_trace()
    print(" Google User ", google_user)
    # return user
    # login_user(user)
    
    # if google_user is not None:
    #     user = User.authenticate_session_user(google_user)
    #     login_user(user)
        
    # print(f"this is the user in user session {session['user']}")
    
   
    return redirect(url_for('main.profile', user=google_user))
    # if user is None:
    #     return 'Authentication failed'
    # elif user['email_verified'] is not True:
    #     return 'Email not verified by Google.', 400
    # else:
    # #     try:
    # #         if User.get(user['sub']) is not None and User.get(user['sub']) is not False:
    # #             return redirect(url_for('main.profile', user=current_user))
    # #         else:
    # #             user = User.get(user['sub'])
    # #             login_user(user)
    # #     except Exception as e:
    # #         print(e)
    # #         return 'Authentication failed'
    #     return redirect(url_for('main.profile', user=user))


# @auth.route('/protected_area')
# @login_is_required
# def protected_area():
#     return 'This is a protected area'

@auth.route('/google/auth/callback')
def google_auth_callback():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(user)
    return user

