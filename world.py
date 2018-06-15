import random
import currentstate
import missions

class World(object):
    def __init__(self):
        """
        A World is a dictionary of regions, initialized to specific values
        """
        # Creates the Facility
        self.facility=Facility()

        # Defines the global geoscheme
        self.northAmerica=Region("North America",-20)
        self.southAmerica=Region("South America",0)
        self.europe=Region("Europe",-20)
        self.asia=Region("Asia",+10)
        self.africa=Region("Africa",+20)
        self.australia=Region("Australia",+20)
        # Packs the regions into a list for easy traversal
        self.regions=[
            self.northAmerica, 
            self.southAmerica, 
            self.europe, 
            self.asia,
            self.africa, 
            self.australia
        ]

class Region(object):
    def __init__(self, name, difficulty):
        """
        A region is an area in the game's world where missions can be performed,
        employees can be hired, and subjects can be found and extracted.
        """
        self.name=name
        self.difficulty=difficulty
        self.heat=0

        # The array of subjects in the region
        self.subjects=[]
        # The array of soldiers in the region
        self.soldiers=[]
        # The array of scientists in the region
        self.scientists=[]
        
        # Each type of mission is an object that holds each available mission of that type for the region
        self.recruitMissions=missions.MissionType("recruit")
        self.reconMissions=missions.MissionType("recon")
        self.extractMissions=missions.MissionType("extract")
        self.damConMissions=missions.MissionType("damCon")

        # The list of MissionTypes for the region, so that all missions can be traversed
        self.missionTypes=[
            self.recruitMissions,
            self.reconMissions,
            self.extractMissions,
            self.damConMissions
        ]

        print("regioncreate", self.name)

    def generatePeople(self):
        """
        Generate a number of hireable people in the region based on the tier, and whose stats are based on the tier
        This is called at the end of each month
        """
        self.generateEmployees()
        self.generateSubjects()

    def generateEmployees(self):
        # The amount of employees generated should be based on the tier
        numberOfEmployeesToGenerate=random.randint(1,currentstate.gamestate.tier+1)
        for x in range(numberOfEmployeesToGenerate):
            x

    def generateSubjects(self):
        pass

    def generateMissions(self):
        pass


class Facility(Region):
    def __init__(self):
        Region.__init__(self, "Base", 0)
        """
        The facility object represents the player's base of operations. 
        This is where data about what is in the facility is stored, such as hired and hireable employees and rooms
        """
        

        print("facilitycreate")
