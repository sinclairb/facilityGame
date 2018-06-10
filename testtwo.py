class State(object):
    def __init__(self):
        self.player=Player()
        self.facility=Facility()
        self.facility.hireList.append(self.player)
        self.facility.hireList2.append(self.player)
        print("statecreate")


class Facility(object):
    def __init__(self):
        self.hireList=[]
        self.hireList2=[]
        print("facilitycreate")


class Player(object):
    def __init__(self):
        self.name="Bob Barker"
        print("playercreate",self.name)


class Soldier(object):
    def __init__(self):
        self.name="Dirk Valentine"
        print("soldiercreate",self.name)

newState=State()
print(newState.facility.hireList[0].name)
newState.facility.hireList[0].name="NOT Bob Barker"
print(newState.facility.hireList2[0].name)
print(newState.facility.hireList[0].name)
print(newState.player.name)

"""
for character in newState.facility.hireList:
    print(character.name)

generatedSoldier=Soldier()
newState.facility.hireList.append(generatedSoldier)

for character in newState.facility.hireList:
    print(character.name)

x=1
for character in newState.facility.hireList:
    character.name="NEW NAME"+str(x)
    x+=1

for character in newState.facility.hireList:
    print(character.name)

print(generatedSoldier.name)
print(newState.player.name)
"""