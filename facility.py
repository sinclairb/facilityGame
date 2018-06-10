class Facility(object):
    def __init__(self):
        """
        The facility object represents the player's base of operations. 
        This is where data about what is in the facility is stored, such as hired and hireable employees and rooms
        For the sake of standardization, hired means working and useable within the facility
        """
        # The array of hired subjects
        self.subjects=[]
        # The array of hired soldiers
        self.soldiers=[]
        # The array of hired scientists
        self.scientists=[]

        print("facilitycreate")

