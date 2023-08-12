from app.auth import auth
from flask import render_template, abort, session, redirect, url_for
from app.extensions import oauth, login, db
import os
from authlib.common.security import generate_token
from app.helpers import login_is_required
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)



@auth.route('/login')
def login():
    return render_template('login.html')



# @auth.route('/logout')
# def logout():
    
#     return render_template('logout.html')


# @auth.route('/google/')
# def google():
#     # import the google client id and secret from the environment variables
#     GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
#     GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

#     CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
#     oauth.register(
#         name='google',
#         client_id=GOOGLE_CLIENT_ID,
#         client_secret=GOOGLE_CLIENT_SECRET,
#         server_metadata_url=CONF_URL,
#         client_kwargs={
#             'scope': 'openid email profile'
#         }
#     )

#     # Redirect to google_auth function
#     redirect_uri = url_for('auth.google_auth', _external=True)
#     print(redirect_uri)
#     session['nonce'] = generate_token()
#     # import pdb; pdb.set_trace()
#     return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

# #FIXME - this is not working 304 error when attempting to login with google 
# #NOTE - Something in relation to the redirect_uri and token and that the google client can not be found.
# @auth.route('/google/auth/')
# def google_auth():
#     token = oauth.google.authorize_access_token()
#     # user = oauth.google.parse_id_token(token)
#     user = oauth.google.parse_id_token(token, nonce=session['nonce'])
#     session['user'] = user
#     # import pdb; pdb.set_trace()
#     print(" Google User ", user)
#     # return redirect('/')
#     return redirect(url_for('main.profile', user=user))


# @auth.route('/protected_area')
# @login_is_required
# def protected_area():
#     return 'This is a protected area'