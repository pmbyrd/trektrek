"""This module contains the Star Trek models for the database."""


from app.extensions import db


class Animal(db.Model):
    """Creates an instance of animal for the table in the database"""

    __tablename__ = "animals"

    name = db.Column(db.Text, nullable=False)

    uid = db.Column(db.Text, primary_key=True)

    earthAnimal = db.Column(db.Boolean, nullable=False)

    earthInsect = db.Column(db.Boolean, nullable=False)

    avian = db.Column(db.Boolean, nullable=False)

    canine = db.Column(db.Boolean, nullable=False)

    feline = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Animal #{self.uid}: name = {self.name}>"


class AstronomicalObject(db.Model):
    """Creates an instance of an astronomical object for the database."""

    __tablename__ = "astronomicalObjects"

    uid = db.Column(db.Text, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    astronomicalObjectType = db.Column(db.Text, nullable=True)

    location = db.Column(db.JSON)

    def __repr__(self):
        return f"<AstronomicalObject #{self.uid} name = {self.name}>, location = {self.location}>"

    @classmethod
    def get_all_alpha(cls):
        # Query for all AstronomicalObjects with a location containing "Alpha Quadrant"
        objects_in_alpha_quadrant = cls.query.filter(
            cls.location.cast(db.Text).ilike(
                "%Alpha Quadrant%"
            )  # ANCHOR - cast os used to cast the JSON object to a string
        ).all()
        return objects_in_alpha_quadrant

    @classmethod
    def get_all_beta(cls):
        objects_in_beta_quadrant = cls.query.filter(
            cls.location.cast(db.Text).ilike("%Beta Quadrant%")
        ).all()
        return objects_in_beta_quadrant

    @classmethod
    def get_all_gamma(cls):
        objects_in_gamma_quadrant = cls.query.filter(
            cls.location.cast(db.Text).ilike("%Gamma Quadrant%")
        ).all()
        return objects_in_gamma_quadrant

    @classmethod
    def get_all_delta(cls):
        objects_in_delta_quadrant = cls.query.filter(
            cls.location.cast(db.Text).ilike("%Delta Quadrant%")
        ).all()
        return objects_in_delta_quadrant


class Character(db.Model):
    """Creates an instance of a character for the database."""

    #
    __tablename__ = "characters"
    #
    uid = db.Column(db.Text, primary_key=True)
    #
    name = db.Column(db.Text, nullable=False)
    #
    gender = db.Column(db.Text, nullable=True)
    #
    yearOfBirth = db.Column(db.Integer, nullable=True)
    #
    monthOfBirth = db.Column(db.Integer, nullable=True)
    #
    dayOfBirth = db.Column(db.Integer, nullable=True)
    #
    placeOfBirth = db.Column(db.Text, nullable=True)
    #
    yearOfDeath = db.Column(db.Integer, nullable=True)
    #
    monthOfDeath = db.Column(db.Integer, nullable=True)
    #
    dayOfDeath = db.Column(db.Integer, nullable=True)
    #
    placeOfDeath = db.Column(db.Text, nullable=True)
    #
    height = db.Column(db.Integer, nullable=True)
    #
    weight = db.Column(db.Integer, nullable=True)
    #
    deceased = db.Column(db.Boolean, nullable=True)
    #
    bloodType = db.Column(db.Text, nullable=True)
    #
    maritalStatus = db.Column(db.Text, nullable=True)
    #
    serialNumber = db.Column(db.Text, nullable=True)
    #
    hologramActivationDate = db.Column(db.Integer, nullable=True)
    #
    hologramStatus = db.Column(db.Text, nullable=True)
    #
    hologram = db.Column(db.Boolean, nullable=True)
    #
    fictionalCharacter = db.Column(db.Boolean, nullable=True)
    #
    mirror = db.Column(db.Boolean, nullable=True)
    #
    alternateReality = db.Column(db.Boolean, nullable=True)
    #
    hologramDateStatus = db.Column(db.Integer, nullable=True)
    #

    def __repr__(self):
        return f"<Character #{self.uid}: name = {self.name}>"

    # create relationships to various tables
    species_uid = db.Column(db.String, db.ForeignKey("species.uid"), nullable=True)
    species = db.relationship("Species", backref="characters", lazy=True)

    location_uid = db.Column(db.String, db.ForeignKey("locations.uid"), nullable=True)
    location = db.relationship("Location", backref="characters", lazy=True)


class Performer(db.Model):
    """Creates an instance of a performer for the database."""

    __tablename__ = "performers"

    uid = db.Column(db.Text, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    birthName = db.Column(db.Text, nullable=True)

    gender = db.Column(db.Text, nullable=True)

    dateOfBirth = db.Column(db.Text, nullable=True)

    placeOfBirth = db.Column(db.Text, nullable=True)

    dateOfDeath = db.Column(db.Text, nullable=True)

    placeOfDeath = db.Column(db.Text, nullable=True)

    animalPerformer = db.Column(db.Boolean, nullable=False)

    disPerformer = db.Column(db.Boolean, nullable=False)

    ds9Performer = db.Column(db.Boolean, nullable=False)

    entPerformer = db.Column(db.Boolean, nullable=False)

    filmPerformer = db.Column(db.Boolean, nullable=False)

    standInPerformer = db.Column(db.Boolean, nullable=False)

    stuntPerformer = db.Column(db.Boolean, nullable=False)

    tasPerformer = db.Column(db.Boolean, nullable=False)

    tngPerformer = db.Column(db.Boolean, nullable=False)

    tosPerformer = db.Column(db.Boolean, nullable=False)

    videoGamePerformer = db.Column(db.Boolean, nullable=False)

    voicePerformer = db.Column(db.Boolean, nullable=False)

    voyPerformer = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Performer #{self.uid}: name = {self.name}>"


class Title(db.Model):
    """Creates an instance of a title for the database."""

    __tablename__ = "titles"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    militaryRank = db.Column(db.Boolean, nullable=False)

    fleetRank = db.Column(db.Boolean, nullable=False)

    religiousTitle = db.Column(db.Boolean, nullable=False)

    position = db.Column(db.Boolean, nullable=False)

    mirror = db.Column(db.Boolean, nullable=False)

    # Create a representation of the object
    def __repr__(self):
        return f"<Title #{self.uid}: name = {self.name}>"


class Location(db.Model):
    """Creates an instance of a location for the database."""

    __tablename__ = "locations"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    earthlyLocation = db.Column(db.Boolean, nullable=False)

    fictionalLocation = db.Column(db.Boolean, nullable=False)

    religiousLocation = db.Column(db.Boolean, nullable=False)

    geographicalLocation = db.Column(db.Boolean, nullable=False)

    bodyOfWater = db.Column(db.Boolean, nullable=False)

    country = db.Column(db.Boolean, nullable=False)

    subnationalEntity = db.Column(db.Boolean, nullable=False)

    settlement = db.Column(db.Boolean, nullable=False)

    usSettlement = db.Column(db.Boolean, nullable=False)

    bajoranSettlement = db.Column(db.Boolean, nullable=False)

    colony = db.Column(db.Boolean, nullable=False)

    landform = db.Column(db.Boolean, nullable=False)

    landmark = db.Column(db.Boolean, nullable=False)

    road = db.Column(db.Boolean, nullable=False)

    structure = db.Column(db.Boolean, nullable=False)

    shipyard = db.Column(db.Boolean, nullable=False)

    buildingInterior = db.Column(db.Boolean, nullable=False)

    establishment = db.Column(db.Boolean, nullable=False)

    medicalEstablishment = db.Column(db.Boolean, nullable=False)

    ds9Establishment = db.Column(db.Boolean, nullable=False)

    school = db.Column(db.Boolean, nullable=False)

    mirror = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Location #{self.uid}: name = {self.name}>"


class Conflict(db.Model):
    """Creates an instance of a conflict for the database."""

    __tablename__ = "conflicts"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    yearFrom = db.Column(db.Integer, nullable=True)

    yearTo = db.Column(db.Integer, nullable=True)

    earthConflict = db.Column(db.Boolean, nullable=False)

    federationWar = db.Column(db.Boolean, nullable=False)

    klingonWar = db.Column(db.Boolean, nullable=False)

    dominionWarBattle = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Conflict #{self.uid}: name = {self.name}>, yearFrom = {self.yearFrom}, yearTo = {self.yearTo}>"


class Element(db.Model):
    """Creates an instance of an element found in the Star Trek universe for the database."""

    __tablename__ = "elements"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    symbol = db.Column(db.Text, nullable=True)

    atomicNumber = db.Column(db.Integer, nullable=True)

    atomicWeight = db.Column(db.Integer, nullable=True)

    transuranium = db.Column(db.Boolean, nullable=False)

    gammaSeries = db.Column(db.Boolean, nullable=False)

    hypersonicSeries = db.Column(db.Boolean, nullable=False)

    megaSeries = db.Column(db.Boolean, nullable=False)

    omegaSeries = db.Column(db.Boolean, nullable=False)

    transonicSeries = db.Column(db.Boolean, nullable=False)

    worldSeries = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Element #{self.uid}: name = {self.name}>, symbol = {self.symbol}, atomicNumber = {self.atomicNumber}, atomicWeight = {self.atomicWeight}>"


class Weapon(db.Model):
    """Creates an instance of a weapon for the database."""

    __tablename__ = "weapons"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    handHeldWeapon = db.Column(db.Boolean, nullable=False)

    laserTechnology = db.Column(db.Boolean, nullable=False)

    plasmaTechnology = db.Column(db.Boolean, nullable=False)

    worldSeries = db.Column(db.Boolean, nullable=True)

    photonicTechnology = db.Column(db.Boolean, nullable=False)

    phaserTechnology = db.Column(db.Boolean, nullable=False)

    mirror = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Weapon #{self.uid}: name = {self.name}>"


class Food(db.Model):
    """Creates an instance of a food for the database."""

    __tablename__ = "foods"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    earthlyOrigin = db.Column(db.Boolean, nullable=False)

    dessert = db.Column(db.Boolean, nullable=False)

    fruit = db.Column(db.Boolean, nullable=False)

    herbOrSpice = db.Column(db.Boolean, nullable=False)

    sauce = db.Column(db.Boolean, nullable=False)

    soup = db.Column(db.Boolean, nullable=False)

    beverage = db.Column(db.Boolean, nullable=False)

    alcoholicBeverage = db.Column(db.Boolean, nullable=False)

    juice = db.Column(db.Boolean, nullable=False)

    tea = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Food #{self.uid}: name = {self.name}>"


class Technology(db.Model):
    """Creates an instance of a technology for the database."""

    __tablename__ = "technologies"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    borgTechnology = db.Column(db.Boolean, nullable=False)

    borgComponent = db.Column(db.Boolean, nullable=False)

    communicationsTechnology = db.Column(db.Boolean, nullable=False)

    computerTechnology = db.Column(db.Boolean, nullable=False)

    computerProgramming = db.Column(db.Boolean, nullable=False)

    subroutine = db.Column(db.Boolean, nullable=False)

    database = db.Column(db.Boolean, nullable=False)

    energyTechnology = db.Column(db.Boolean, nullable=False)

    fictionalTechnology = db.Column(db.Boolean, nullable=False)

    holographicTechnology = db.Column(db.Boolean, nullable=False)

    identificationTechnology = db.Column(db.Boolean, nullable=False)

    lifeSupportTechnology = db.Column(db.Boolean, nullable=False)

    sensorTechnology = db.Column(db.Boolean, nullable=False)

    shieldTechnology = db.Column(db.Boolean, nullable=False)

    tool = db.Column(db.Boolean, nullable=False)

    culinaryTool = db.Column(db.Boolean, nullable=False)

    engineeringTool = db.Column(db.Boolean, nullable=False)

    householdTool = db.Column(db.Boolean, nullable=False)

    medicalEquipment = db.Column(db.Boolean, nullable=False)

    transporterTechnology = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Technology #{self.uid}: name = {self.name}>"


class Company(db.Model):
    """Creates an instance of a company for the database."""

    __tablename__ = "companies"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    broadcaster = db.Column(db.Boolean, nullable=False)

    collectibleCompany = db.Column(db.Boolean, nullable=False)

    conglomerate = db.Column(db.Boolean, nullable=False)

    digitalVisualEffectsCompany = db.Column(db.Boolean, nullable=False)

    distributor = db.Column(db.Boolean, nullable=False)

    gameCompany = db.Column(db.Boolean, nullable=False)

    filmEquipmentCompany = db.Column(db.Boolean, nullable=False)

    makeUpEffectsStudio = db.Column(db.Boolean, nullable=False)

    mattePaintingCompany = db.Column(db.Boolean, nullable=False)

    modelAndMiniatureEffectsCompany = db.Column(db.Boolean, nullable=False)

    postProductionCompany = db.Column(db.Boolean, nullable=False)

    productionCompany = db.Column(db.Boolean, nullable=False)

    propCompany = db.Column(db.Boolean, nullable=False)

    recordLabel = db.Column(db.Boolean, nullable=False)

    specialEffectsCompany = db.Column(db.Boolean, nullable=False)

    tvAndFilmProductionCompany = db.Column(db.Boolean, nullable=False)

    videoGameCompany = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Company #{self.uid}: name = {self.name}>"


class Staff(db.Model):
    """Creates an instace of a staff member for the database."""

    __tablename__ = "staff"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    birthName = db.Column(db.Text, nullable=True)

    gender = db.Column(db.Text, nullable=True)

    dateOfBirth = db.Column(db.Text, nullable=True)

    placeOfBirth = db.Column(db.Text, nullable=True)

    dateOfDeath = db.Column(db.Text, nullable=True)

    placeOfDeath = db.Column(db.Text, nullable=True)

    artDepartment = db.Column(db.Boolean, nullable=False)

    artDirector = db.Column(db.Boolean, nullable=False)

    productionDesigner = db.Column(db.Boolean, nullable=False)

    cameraAndElectricalDepartment = db.Column(db.Boolean, nullable=False)

    cinematographer = db.Column(db.Boolean, nullable=False)

    castingDepartment = db.Column(db.Boolean, nullable=False)

    costumeDepartment = db.Column(db.Boolean, nullable=False)

    costumeDesigner = db.Column(db.Boolean, nullable=False)

    director = db.Column(db.Boolean, nullable=False)

    assistantOrSecondUnitDirector = db.Column(db.Boolean, nullable=False)

    exhibitAndAttractionStaff = db.Column(db.Boolean, nullable=False)

    filmEditor = db.Column(db.Boolean, nullable=False)

    linguist = db.Column(db.Boolean, nullable=False)

    locationStaff = db.Column(db.Boolean, nullable=False)

    makeupStaff = db.Column(db.Boolean, nullable=False)

    musicDepartment = db.Column(db.Boolean, nullable=False)

    composer = db.Column(db.Boolean, nullable=False)

    personalAssistant = db.Column(db.Boolean, nullable=False)

    producer = db.Column(db.Boolean, nullable=False)

    productionAssociate = db.Column(db.Boolean, nullable=False)

    productionStaff = db.Column(db.Boolean, nullable=False)

    publicationStaff = db.Column(db.Boolean, nullable=False)

    scienceConsultant = db.Column(db.Boolean, nullable=False)

    soundDepartment = db.Column(db.Boolean, nullable=False)

    specialAndVisualEffectsStaff = db.Column(db.Boolean, nullable=False)

    author = db.Column(db.Boolean, nullable=False)

    audioAuthor = db.Column(db.Boolean, nullable=False)

    calendarArtist = db.Column(db.Boolean, nullable=False)

    comicArtist = db.Column(db.Boolean, nullable=False)

    comicAuthor = db.Column(db.Boolean, nullable=False)

    comicColorArtist = db.Column(db.Boolean, nullable=False)

    comicInteriorArtist = db.Column(db.Boolean, nullable=False)

    comicInkArtist = db.Column(db.Boolean, nullable=False)

    comicPencilArtist = db.Column(db.Boolean, nullable=False)

    comicLetterArtist = db.Column(db.Boolean, nullable=False)

    comicStripArtist = db.Column(db.Boolean, nullable=False)

    gameArtist = db.Column(db.Boolean, nullable=False)

    gameAuthor = db.Column(db.Boolean, nullable=False)

    novelArtist = db.Column(db.Boolean, nullable=False)

    novelAuthor = db.Column(db.Boolean, nullable=False)

    referenceArtist = db.Column(db.Boolean, nullable=False)

    referenceAuthor = db.Column(db.Boolean, nullable=False)

    publicationArtist = db.Column(db.Boolean, nullable=False)

    publicationDesigner = db.Column(db.Boolean, nullable=False)

    publicationEditor = db.Column(db.Boolean, nullable=False)

    publicityArtist = db.Column(db.Boolean, nullable=False)

    cbsDigitalStaff = db.Column(db.Boolean, nullable=False)

    ilmProductionStaff = db.Column(db.Boolean, nullable=False)

    specialFeaturesStaff = db.Column(db.Boolean, nullable=False)

    storyEditor = db.Column(db.Boolean, nullable=False)

    studioExecutive = db.Column(db.Boolean, nullable=False)

    stuntDepartment = db.Column(db.Boolean, nullable=False)

    transportationDepartment = db.Column(db.Boolean, nullable=False)

    videoGameProductionStaff = db.Column(db.Boolean, nullable=False)

    writer = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Staff #{self.uid}: name = {self.name}>"


class Species(db.Model):
    """Creates an instance of a species from the Star Trek universe for the database"""

    # *homeworld must reference a planet in the Planets table, quadrant must also be a referenced to the astronomical quadrant of the planet

    __tablename__ = "species"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    homeworld = db.Column(db.JSON, nullable=True)

    quadrant = db.Column(db.JSON, nullable=True)

    extinctSpecies = db.Column(db.Boolean, nullable=False)

    warpCapableSpecies = db.Column(db.Boolean, nullable=False)

    extraGalacticSpecies = db.Column(db.Boolean, nullable=False)

    humanoidSpecies = db.Column(db.Boolean, nullable=False)

    reptilianSpecies = db.Column(db.Boolean, nullable=False)

    nonCorporealSpecies = db.Column(db.Boolean, nullable=False)

    shapeshiftingSpecies = db.Column(db.Boolean, nullable=False)

    spaceborneSpecies = db.Column(db.Boolean, nullable=False)

    telepathicSpecies = db.Column(db.Boolean, nullable=False)

    transDimensionalSpecies = db.Column(db.Boolean, nullable=False)

    unnamedSpecies = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    # *homeworld and quadrant must be referenced to the astronomicalObjects table when not null it is a foreign key the data is json and must handle the reading the data from the json object
    astronomicalObjects_uid = db.Column(
        db.String, db.ForeignKey("astronomicalObjects.uid"), nullable=True
    )

    def __repr__(self):
        return f"<Species #{self.uid}: name = {self.name}>, homeworld = {self.homeworld}, quadrant = {self.quadrant}>"

    def get_species_by_quadrant(self):
        pass


class Organization(db.Model):
    """Creates an instance of an organization from the Star Trek universe for the database"""

    __tablename__ = "organizations"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    government = db.Column(db.Boolean, nullable=False)

    intergovernmentalOrganization = db.Column(db.Boolean, nullable=False)

    researchOrganization = db.Column(db.Boolean, nullable=False)

    sportOrganization = db.Column(db.Boolean, nullable=False)

    medicalOrganization = db.Column(db.Boolean, nullable=False)

    militaryOrganization = db.Column(db.Boolean, nullable=False)

    militaryUnit = db.Column(db.Boolean, nullable=False)

    governmentAgency = db.Column(db.Boolean, nullable=False)

    lawEnforcementAgency = db.Column(db.Boolean, nullable=False)

    prisonOrPenalColony = db.Column(db.Boolean, nullable=False)

    mirror = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Organization #{self.uid}: name = {self.name}>, government = {self.government}"


class Occupation(db.Model):
    """Creates an instance of an occupation from the Star Trek universe for the database"""

    __tablename__ = "occupations"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    legalOccupation = db.Column(db.Boolean, nullable=False)

    medicalOccupation = db.Column(db.Boolean, nullable=False)

    scientificOccupation = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Occupation #{self.uid}: name = {self.name}>"


class SpacecraftClass(db.Model):
    """Creates an instance of a spacecraft class from the Star Trek universe for the database these classes are used to create the spacecraft table"""

    __tablename__ = "spacecraftClasses"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    numberOfDecks = db.Column(db.Integer, nullable=True)

    warpCapable = db.Column(db.Boolean, nullable=False)

    alternateReality = db.Column(db.Boolean, nullable=False)

    activeFrom = db.Column(db.Text, nullable=True)

    activeTo = db.Column(db.Text, nullable=True)

    species = db.Column(db.JSON, nullable=True)

    species_uid = db.Column(db.String, db.ForeignKey("species.uid"), nullable=True)

    owner = db.Column(db.Text, nullable=True)

    operator = db.Column(db.Text, nullable=True)

    affiliation = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<SpacecraftClass #{self.uid}: name = {self.name}>, species = {self.species}>, affiliation = {self.affiliation}>"


# !critcal need to fix the Spacecraft class, overwrote the correct file with the incorrect file


class Spacecraft(db.Model):
    """Creates an instance of a spacecraft from the Star Trek universe for the database"""

    __tablename__ = "spacecraft"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    registry = db.Column(db.Text, nullable=True)

    status = db.Column(db.Text, nullable=True)

    dateStatus = db.Column(db.Text, nullable=True)

    spacecraftClass_uid = db.Column(
        db.String, db.ForeignKey(SpacecraftClass.uid), nullable=True
    )

    spacecraft_class = db.relationship(
        "SpacecraftClass", backref="spacecraft", lazy=True
    )

    spacecraftClass = db.Column(db.JSON, nullable=True)

    # !Owner and operator must be referenced to the organizations table when not null it is a foreign key the data is json and must handle the reading the data from the json object
    owner = db.Column(db.JSON, nullable=True)

    orginization_uid = db.Column(
        db.String, db.ForeignKey("organizations.uid"), nullable=True
    )

    operator = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f"<Spacecraft #{self.uid}: name = {self.name}>, registry = {self.registry}, status = {self.status}, dateStatus = {self.dateStatus}, spacecraftClass = {self.spacecraftClass}, owner = {self.owner}, operator = {self.operator}>"


class Material(db.Model):
    """Creates an instance of a material from the Star Trek universe for the database"""

    __tablename__ = "materials"

    uid = db.Column(db.String, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    chemicalCompound = db.Column(db.Boolean, nullable=False)

    biochemicalCompound = db.Column(db.Boolean, nullable=False)

    drug = db.Column(db.Boolean, nullable=False)

    poisonousSubstance = db.Column(db.Boolean, nullable=False)

    explosive = db.Column(db.Boolean, nullable=False)

    gemstone = db.Column(db.Boolean, nullable=False)

    alloyOrComposite = db.Column(db.Boolean, nullable=False)

    fuel = db.Column(db.Boolean, nullable=False)

    mineral = db.Column(db.Boolean, nullable=False)

    preciousMaterial = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Material #{self.uid} name = {self.name}> "


class Movie(db.Model):
    """Creates an instance of a movie from the Star Trek universe for the database"""

    __tablename__ = "movies"

    uid = db.Column(db.String, primary_key=True)

    title = db.Column(db.Text, nullable=False)

    mainDirector = db.Column(db.JSON, nullable=True)

    staff_uid = db.Column(db.String, db.ForeignKey("staff.uid"), nullable=True)

    titleBulgarian = db.Column(db.Text, nullable=True)

    titleCatalan = db.Column(db.Text, nullable=True)

    titleChineseTraditional = db.Column(db.Text, nullable=True)

    titleGerman = db.Column(db.Text, nullable=True)

    titleItalian = db.Column(db.Text, nullable=True)

    titleJapanese = db.Column(db.Text, nullable=True)

    titlePolish = db.Column(db.Text, nullable=True)

    titleRussian = db.Column(db.Text, nullable=True)

    titleSerbian = db.Column(db.Text, nullable=True)

    titleSpanish = db.Column(db.Text, nullable=True)

    stardateFrom = db.Column(db.Text, nullable=True)

    stardateTo = db.Column(db.Text, nullable=True)

    yearFrom = db.Column(db.Text, nullable=True)

    yearTo = db.Column(db.Text, nullable=True)

    usReleaseDate = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Movie #{self.uid} title = {self.title}, releaseDate = {self.usReleaseDate}>"


# Todo load in the shows information by series, season episode in that order


class Series(db.Model):
    """Creates an instance of a series from the Star Trek universe for the database, the series has a relationship with the company table as well as the seasons and episodes table"""

    uid = db.Column(db.String, primary_key=True)

    title = db.Column(db.Text, nullable=False)

    abbreviation = db.Column(db.Text, nullable=False)

    productionStartYear = db.Column(db.Integer, nullable=True)

    productionEndYear = db.Column(db.Integer, nullable=True)

    originalRunStartDate = db.Column(db.Text, nullable=True)

    originalRunEndDate = db.Column(db.Text, nullable=True)

    seasonsCount = db.Column(db.Integer, nullable=True)

    episodesCount = db.Column(db.Integer, nullable=True)

    featureLengthEpisodesCount = db.Column(db.Integer, nullable=True)

    productionCompany = db.Column(db.JSON, nullable=True)

    originalBroadcaster = db.Column(db.JSON, nullable=True)

    companies_uid = db.Column(db.String, db.ForeignKey("companies.uid"), nullable=True)

    def __repr__(self):
        return f"<Series #{self.uid} title = {self.title}, abbreviation = {self.abbreviation}>"


class Season(db.Model):
    """Creates an instance of a season based off of the series table"""

    uid = db.Column(db.String, primary_key=True)

    title = db.Column(db.Text, nullable=False)

    series = db.Column(db.JSON, nullable=True)

    series_uid = db.Column(db.String, db.ForeignKey("series.uid"), nullable=True)

    seasonNumber = db.Column(db.Integer, nullable=False)

    numberOfEpisodes = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Series: #{self.series}, Season #{self.uid} title = {self.title}, seasonNumber = {self.seasonNumber}>"


class Episode(db.Model):
    """Creates an instance of an episode based off of the season table"""

    uid = db.Column(db.String, primary_key=True)

    title = db.Column(db.Text, nullable=False)

    titleGerman = db.Column(db.Text, nullable=True)

    titleItalian = db.Column(db.Text, nullable=True)

    titleJapanese = db.Column(db.Text, nullable=True)

    series = db.Column(db.JSON, nullable=True)

    season = db.Column(db.JSON, nullable=True)

    seasonNumber = db.Column(db.Integer, nullable=False)

    episodeNumber = db.Column(db.Integer, nullable=False)

    productionSerialNumber = db.Column(db.Text, nullable=False)

    featureLength = db.Column(db.Boolean, nullable=False)

    stardateFrom = db.Column(db.Float, nullable=True)

    stardateTo = db.Column(db.Float, nullable=True)

    yearFrom = db.Column(db.Integer, nullable=True)

    yearTo = db.Column(db.Integer, nullable=True)

    usAirDate = db.Column(db.Text, nullable=True)

    finalScriptDate = db.Column(db.Text, nullable=True)

    series_uid = db.Column(db.String, db.ForeignKey("series.uid"), nullable=True)

    def __repr__(self):
        return f"<Episode #{self.uid} title = {self.title}, episodeNumber = {self.episodeNumber}>"


# create a table that holds information about a show


class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)

    # series_uid = db.Column(db.String, db.ForeignKey('series.uid'), nullable=True)

