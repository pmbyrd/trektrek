"""_
Summary_ : This is the blueprint for the authentication module.
"""

from flask import Blueprint

auth = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static',
    url_prefix='/auth'
)

from app.auth import routes
