import character
import world
import facility

# This class can be passed or referenced in order to load values that define the state of the game
# These values are what are saved and loaded
class Gamestate(object):
    # The init method creates a gamestate that is set up for a new game
    def __init__(self):
        # Tier measures how much the player has advanced.
        # The higher the tier, the higher level employees, subjects, and events occur
        self.tier=0

        # Defines the global geoscheme
        self.northAmerica=world.Region("North America",-20)
        self.southAmerica=world.Region("South America",0)
        self.europe=world.Region("Europe",-20)
        self.asia=world.Region("Asia",+10)
        self.africa=world.Region("Africa",+20)
        self.australia=world.Region("Australia",+20)
        # Packs the regions into a dictionary for easy traversal
        self.regions={
            self.northAmerica.name:self.northAmerica,
            self.southAmerica.name:self.southAmerica,
            self.europe.name:self.europe,
            self.asia.name:self.asia,
            self.africa.name:self.africa,
            self.australia.name:self.australia}
        # Create the facility and set its location
        self.facility=facility.Facility()

        # The amount of money available to the player
        self.funds=1000000
        # The current date, only the weeks matter
        self.week=0

        # The amount of global heat, serves as a modifier on mission difficulty
        # Each region also has local heat
        self.globalHeat=0

        # The player object
        self.player=character.Player()

