"""Summary: This file contains the routes for the universe blueprint.

This file defines the routes for various endpoints related to the universe blueprint.
It includes routes for testing, rendering templates, and retrieving data from the database.
Each route is responsible for rendering the appropriate template or returning the requested data.

"""

# Make sure to import the blueprint
from flask import jsonify, render_template, request
from app.helpers import MemoryAlphaScraper, replace_space
from app.universe import universe
from app.models.star_trek_models import Animal, Material, Title, AstronomicalObject, Character,Food, Element, Location, Conflict, Occupation, Organization, SpacecraftClass, Spacecraft, Species, Technology, Weapon


@universe.route('/test')
def testing():
    """Test route"""
    return "Testing the universe blueprint"

@universe.route('/')
def index():
    """Renders the index page"""
    return render_template('universe.html')

@universe.route('/animals')
def animals():
    """Returns all animals in the database"""
    page = request.args.get('page', 1, type=int)
    animals = Animal.query.order_by(Animal.name.asc()).all()
    paginated_animals = Animal.query.order_by(Animal.name.asc()).paginate(page=page, per_page=25)
    return render_template('animals.html', animals=animals, title='Animals', page=page, paginated_animals=paginated_animals)

@universe.route('/animal/<name>')
def animal(name):
    """Returns a single animal from the database"""
    animal = Animal.query.filter_by(name=name).first()
    if animal:
        scrapped_animal = MemoryAlphaScraper(replace_space(name))
        summary = scrapped_animal.get_summary()
        if summary:
            return render_template('animal.html', animal=animal, summary=summary, title=name)
        else:
            print("summary not found")
            raise TypeError
    return render_template('animal.html', animal=animal, title=name)

@universe.route('/astronomical_objects')
def astronomical_objects():
    """Returns all astronomical objects in the database"""
    page = request.args.get('page', 1, type=int)
    astronomical_objects = AstronomicalObject.query.order_by(AstronomicalObject.name.asc()).all()
    paginated_astronomical_objects = AstronomicalObject.query.order_by(AstronomicalObject.name.asc()).paginate(page=page, per_page=25)
    return render_template('astronomical_objects.html', astronomical_objects=astronomical_objects, title='Astronomical Objects', page=page, paginated_astronomical_objects=paginated_astronomical_objects)

@universe.route('/astronomical_objects/<name>')
def astronomical_object(name):
    """Returns a single astronomical object from the database"""
    astronomical_object = AstronomicalObject.query.filter_by(name=name).first()
    if astronomical_object:
        try:
            scrapped_astronomical_object = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_astronomical_object.get_summary()
            if summary:
                return render_template('astronomical_object.html', astronomical_object=astronomical_object, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/characters')
def characters():
    """Returns all characters in the database"""
    page = request.args.get('page', 1, type=int)
    characters = Character.query.order_by(Character.name.asc()).all()
    paginated_characters = Character.query.order_by(Character.name.asc()).paginate(page=page, per_page=25)
    return render_template('characters.html', characters=characters, title='Characters', page=page, paginated_characters=paginated_characters)

@universe.route('/characters/<name>')
def character(name):
    """Returns a single character from the database"""
    character = Character.query.filter_by(name=name).first()
    try:
        scrapped_character = MemoryAlphaScraper(replace_space(name))
        summary = scrapped_character.get_summary()
        if summary:
            return render_template('character.html', character=character, summary=summary, title=name)
        else:
            print("summary not found")
            raise TypeError
    except Exception as e:
        return "Error: " + str(e)


    
@universe.route('/conflicts')
def conflicts():
    """Returns all conflicts in the database"""
    page = request.args.get('page', 1, type=int)
    conflict = Conflict.query.order_by(Conflict.name.asc()).all()
    paginated_conflicts = Conflict.query.order_by(Conflict.name.asc()).paginate(page=page, per_page=25)
    return render_template('conflicts.html', conflict=conflict, title='Conflicts', page=page, paginated_conflicts=paginated_conflicts)

@universe.route('/conflicts/<name>')
def conflict(name):
    """Returns a single conflict from the database"""
    conflict = Conflict.query.filter_by(name=name).first()
    if conflict:
        try:
            scrapped_conflict = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_conflict.get_summary()
            if summary:
                return render_template('conflict.html', conflict=conflict, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/elements')
def elements():
    """Returns all elements in the database"""
    page = request.args.get('page', 1, type=int)
    elements = Element.query.order_by(Element.name.asc()).all()
    paginated_elements = Element.query.order_by(Element.name.asc()).paginate(page=page, per_page=25)
    return render_template('elements.html', elements=elements, title='Elements', page=page, paginated_elements=paginated_elements)

@universe.route('/elements/<name>')
def element(name):
    """Returns a single element from the database"""
    element = Element.query.filter_by(name=name).first()
    if element:
        try:
            scrapped_element = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_element.get_summary()
            if summary:
                return render_template('element.html', element=element, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/foods')
def foods():
    """Returns all foods in the database"""
    page = request.args.get('page', 1, type=int)
    foods = Food.query.order_by(Food.name.asc()).all()
    paginated_foods = Food.query.order_by(Food.name.asc()).paginate(page=page, per_page=25)
    return render_template('foods.html', foods=foods, title='Foods', page=page, paginated_foods=paginated_foods)

@universe.route('/foods/<name>')
def food(name):
    """Returns a single food from the database"""
    food = Food.query.filter_by(name=name).first()
    if food:
        try:
            scrapped_food = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_food.get_summary()
            if summary:
                return render_template('food.html', food=food, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/locations')
def locations():
    """Returns all locations in the database"""
    page = request.args.get('page', 1, type=int)
    locations = Location.query.order_by(Location.name.asc()).all()
    paginated_locations = Location.query.order_by(Location.name.asc()).paginate(page=page, per_page=25)
    return render_template('locations.html', locations=locations, title='Locations', page=page, paginated_locations=paginated_locations)

@universe.route('/locations/<name>')
def location(name):
    """Returns a single location from the database"""
    location = Location.query.filter_by(name=name).first()
    if location:
        try:
            scrapped_location = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_location.get_summary()
            if summary:
                return render_template('location.html', location=location, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/materials')
def materials():
    """Returns all materials in the database"""
    page = request.args.get('page', 1, type=int)
    materials = Material.query.order_by(Material.name.asc()).all()
    paginated_materials = Material.query.order_by(Material.name.asc()).paginate(page=page, per_page=25)
    return render_template('materials.html', materials=materials, title='Materials', page=page, paginated_materials=paginated_materials)

@universe.route('/materials/<name>')
def material(name):
    """Returns a single material from the database"""
    material = Material.query.filter_by(name=name).first()
    if material:
        try:
            scrapped_material = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_material.get_summary()
            if summary:
                return render_template('material.html', material=material, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/occupations')
def occupations():
    """Returns all occupations in the database"""
    page = request.args.get('page', 1, type=int)
    occupations = Occupation.query.order_by(Occupation.name.asc()).all()
    paginated_occupations = Occupation.query.order_by(Occupation.name.asc()).paginate(page=page, per_page=25)
    return render_template('occupations.html', occupations=occupations, title='Occupations', page=page, paginated_occupations=paginated_occupations)

@universe.route('/occupations/<name>')
def occupation(name):
    """Returns a single occupation from the database"""
    occupation = Occupation.query.filter_by(name=name).first()
    if occupation:
        try:
            scrapped_occupation = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_occupation.get_summary()
            if summary:
                return render_template('occupation.html', occupation=occupation, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/organizations')
def organizations():
    """Returns all organizations in the database"""
    page = request.args.get('page', 1, type=int)
    organizations = Organization.query.order_by(Organization.name.asc()).all()
    paginated_organizations = Organization.query.order_by(Organization.name.asc()).paginate(page=page, per_page=25)
    return render_template('organizations.html', organizations=organizations, title='Organizations', page=page, paginated_organizations=paginated_organizations)
    organizations = Organization.query.all()
    paginated_organizations = Organization.query.order_by(Organization.name.asc()).paginate(page=page, per_page=25)
    return render_template('organizations.html', organizations=organizations, title='Organizations', page=page, paginated_organizations=paginated_organizations)

# FIXME - The organizations route is not working at the moment
@universe.route('/organizations/<name>')
def organization(name):
    """Returns a single organization from the database"""
    organization = Organization.query.filter_by(name=name).first()
    if organization:
        try:
            scrapped_organization = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_organization.get_summary()
            if summary:
                return render_template('organization.html', organization=organization, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)
        
@universe.route('/spacecrafts_classes')
def spacecrafts_classes():
    """Returns all spacecraft classes in the database"""
    spacecrafts_classes = SpacecraftClass.query.all()
    page = request.args.get('page', 1, type=int)
    paginated_spacecraft_classes = SpacecraftClass.query.order_by(SpacecraftClass.name.asc()).paginate(page=page, per_page=25)
    return render_template('spacecrafts_classes.html', spacecraft_classes=spacecraft_classes, title='Spacecrafts Classes', page=page, paginated_spacecraft_classes=paginated_spacecraft_classes)

@universe.route('/spacecrafts_classes/<name>')
def spacecraft_class(name):
    """Returns a single spacecraft class from the database"""
    spacecraft_class = SpacecraftClass.query.filter_by(name=name).first()
    if spacecraft_class:
        try:
            scrapped_spacecraft_class = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_spacecraft_class.get_summary()
            if summary:
                return render_template('spacecraft_class.html', spacecraft_class=spacecraft_class, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/spacecrafts')
def spacecrafts():
    """Returns all spacecrafts in the database"""
    spacecrafts = Spacecraft.query.order_by(Spacecraft.name.asc()).all()
    page = request.args.get('page', 1, type=int)
    paginated_spacecrafts = Spacecraft.query.order_by(Spacecraft.name.asc()).paginate(page=page, per_page=25)
    return render_template('spacecrafts.html', spacecrafts=spacecrafts, title='Spacecrafts', page=page, paginated_spacecrafts=paginated_spacecrafts)

@universe.route('/spacecrafts/<name>')
def spacecraft(name):
    """Returns a single spacecraft from the database"""
    spacecraft = Spacecraft.query.filter_by(name=name).first()
    if spacecraft:
        try:
            scrapped_spacecraft = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_spacecraft.get_summary()
            if summary:
                return render_template('spacecraft.html', spacecraft=spacecraft, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/species')
def specieses():
    """Returns all species in the database"""
    specieses = Species.query.order_by(Species.name.asc()).all()
    page = request.args.get('page', 1, type=int)
    paginated_specieses = Species.query.order_by(Species.name.asc()).paginate(page=page, per_page=25)
  
    return render_template('species_all.html', specieses=specieses, title='Species', page=page, paginated_specieses=paginated_specieses)

#FIXME - This route is not working at the moment
@universe.route('/species/<name>')
def species(name):
    """Returns a single species from the database"""
    species = Species.query.filter_by(name=name).first()
    if species:
        try:
            scrapped_species = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_species.get_summary()
            if summary:
                return render_template('species.html', species=species, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)
    
@universe.route('/technologies')
def technologies():
    """Returns all technologies in the database"""
    technologies = Technology.query.order_by(Technology.name.asc()).all()
    page = request.args.get('page', 1, type=int)
    paginated_technologies = Technology.query.order_by(Technology.name.asc()).paginate(page=page, per_page=25)
    return render_template('technologies.html', technologies=technologies, title='Technologies', page=page, paginated_technologies=paginated_technologies)

@universe.route('/technologies/<name>')
def technology(name):
    """Returns a single technology from the database"""
    technology = Technology.query.filter_by(name=name).first()
    if technology:
        try:
            scrapped_technology = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_technology.get_summary()
            if summary:
                return render_template('technology.html', technology=technology, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)

@universe.route('/titles')
def titles():
    """Returns all titles in the database"""
    titles = Title.query.order_by(Title.name.asc()).all()
    page = request.args.get('page', 1, type=int)
    paginated_titles = Title.query.order_by(Title.name.asc()).paginate(page=page, per_page=25)
    return render_template('titles.html', titles=titles, title='Titles', page=page, paginated_titles=paginated_titles)

#FIXME - This route is not working at the moment
@universe.route('/titles/<name>')
def title(name):
    """Returns a single title from the database"""
    title_ = Title.query.filter_by(name=name).first()
    if title_:
        try:
            scrapped_title = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_title.get_summary()
            if summary:
                return render_template('title.html', title_=title_, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)
            
@universe.route('/weapons')
def weapons():
    """Returns all weapons in the database"""
    weapons = Weapon.query.order_by(Weapon.name.asc()).all()
    page = request.args.get('page', 1, type=int)
    paginated_weapons = Weapon.query.order_by(Weapon.name.asc()).paginate(page=page, per_page=25)
    return render_template('weapons.html', weapons=weapons, title = 'Weapons', page=page, paginated_weapons=paginated_weapons)

@universe.route('/weapons/<name>')
def weapon(name):
    """Returns a single weapon from the database"""
    weapon = Weapon.query.filter_by(name=name).first()
    if weapon:
        try:
            scrapped_weapon = MemoryAlphaScraper(replace_space(name))
            summary = scrapped_weapon.get_summary()
            if summary:
                return render_template('weapon.html', weapon=weapon, summary=summary, title=name)
            else:
                print("summary not found")
                raise TypeError
        except Exception as e:
            return "Error: " + str(e)
    return render_template('weapon.html', weapon=weapon, title=name)