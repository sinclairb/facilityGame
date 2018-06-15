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

        # Creates a world, which is a dictionary of regions
        self.world=world.World()

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

