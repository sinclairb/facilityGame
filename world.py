import random
import currentstate

class Region(object):
    def __init__(self, name, difficulty):
        """
        A region is an area in the game's world where missions can be performed,
        employees can be hired, and subjects can be found and extracted.
        """
        self.name=name
        self.difficulty=difficulty
        self.heat=0

        # The array of subjects for "hire"
        self.hireableSubjects=[]
        # The array of soldiers for hire
        self.hireableSoldiers=[]
        # The array of scientists for hire
        self.hireableScientists=[]
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