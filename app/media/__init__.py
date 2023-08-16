"""Summary = This page initializes the media blueprint."""

from flask import Blueprint

media = Blueprint(
    'media', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/media'
    )

from app.media import routes