import random
import currentstate
import names

# A character is a general unspecified person; the template for a player, subject, or employee
# Default values are initialized
class Character(object):
    def __init__(self):
        # Each character has a gender, which determines their pronouns and first name
        self.gender=random.choice(["female","male"])
        # Age in years is used for flavor
        self.age=random.randint(18,70)
        # Birth week determines when a character's birthday is
        # It is arbitrary, but birthdays are important to subjects
        self.birthWeek=random.randint(0,51)
        self.generateName()
        self.generateStats()
        
    def generateName(self):
        if self.gender=="female":
            self.firstName=random.choice(names.femaleFirstNames)
        else:
            self.firstName=random.choice(names.maleFirstNames)
        self.lastName=random.choice(names.lastNames)

    def generateStats(self):
        # Stats are the percent chance of success on a mission (modifiers notwithstanding)
        # Stealth is used for recon, extraction, and damcon
        self.stealth=0
        # Power is used for extraction, guarding, and damcon
        self.power=0
        # Manipulation is used for extraction, damcon, and training
        self.manipulation=0
        # Research is used for recon, research, and training 
        self.research=0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The player object is the player's character
# The player can customize name, age, and stats, to an extent
# Right now, they just default to certain values
class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.stealth=60
        self.power=60
        self.manipulation=60
        self.research=60

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Soldiers have higher power and stealth than other characters
class Soldier(Character):
    def __init__(self):
        Character.__init__(self)
        self.generateStats

    def generateStats(self):
        self.stealth=60
        self.power=60

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Scientists have higher manipulation and research than other characters
class Scientist(Character):
    def __init__(self):
        Character.__init__(self)
        self.generateStats

    def generateStats(self):
        self.manipulation=60
        self.research=60

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Subjects have all higher stats than other characters
# Subjects also have functionality related to being trained
class Subject(Character):
    def __init__(self):
        Character.__init__(self)
        self.generateStats()
        self.generateStatus()

    def generateStats(self):
        self.stealth=60
        self.power=60
        self.manipulation=60
        self.research=60

    def generateStatus(self):
        # How much the subject believes the player will act kindly
        self.trust=0
        # How much the subject believes the player will act unkindly
        self.fear=0
        # How much the subject wants to obey the player
        self.devotion=0
        # How much the subject wants to resist the player
        self.hate=0
        # How much the subject needs the player
        self.dependence=0
        # How much the subject does not need the player
        self.autonomy=0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
