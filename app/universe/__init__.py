"""summary: This file initializes the quadrants blueprint.
    Universe data will include but not limited to the following:
    - Location
    - Character
    - Animals
    - Species
    - Element
    - Conflict
    - Weapon
    - spacecraft
    - spacecraft class
    -astronomical objects
    - food
    - occupation
    - organization
    - technology
    - weapons
"""

from flask import Blueprint

universe = Blueprint(
    'universe', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/universe'   
)

from app.universe import routes