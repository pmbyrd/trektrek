"""
This files initializes the main package.
Handles routes that do not need authentication throughout the application.
"""

from flask import Blueprint

bp = Blueprint('main', __name__)

#NOTE - This import is at the bottom to avoid circular dependencies
from app.main import routes