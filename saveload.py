import datetime
import currentstate
import states

def newGame():
    """
    A new game creates a new gamestate object, which is constructed with default values
    The newly created gamestate object is assigned to the gamestate variable of the currentstate module
    """
    print("Creating New Game",currentstate.gamestate)
    currentstate.gamestate=states.Gamestate()
    print("New Game Created",currentstate.gamestate)

def loadGame(savefile):
    """
    The save game, whose file name is the passed argument "savefile" is loaded into the currentstate
    """
    print("load")

def saveGame():
    """
    The currentstate is written into a save game file, whose file name is the player name, week, and the time of save
    """
    now=datetime.datetime.now()
    dateAndTime=str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+":"+str(now.minute)
    playerName=currentstate.gamestate.player.firstName+currentstate.gamestate.player.lastName
    saveFileName=dateAndTime+playerName+"Week"+str(currentstate.gamestate.week)
    print("saved: ",saveFileName)