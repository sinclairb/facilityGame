import tkinter
import currentstate
import saveload

class LevelFrame(tkinter.Frame):
    def __init__(self, master, nameOfMenuFrame=None):
        tkinter.Frame.__init__(self, master)
        """
        A collection of frames/widgets that are added to the frame passed as the "master" parameter
        A levelFrame consists of a frame that holds menu buttons, and a frame that displays info
        """
        self.grid(row=0,column=0)

        # A frame that holds menu buttons
        self.menuFrame=MenuFrame(self)
        self.menuFrame.grid(row=0,column=0)

        # A frame that holds whatever info should be displayed based on which button in the menuFame was pressed
        # Initialized to an empty frame, but populated via the populateDisplayFrame method
        self.displayFrame=DisplayFrame(self)
        self.displayFrame.grid(row=1,column=0)

        if nameOfMenuFrame:
            self.populateMenuFrame(nameOfMenuFrame)

    def populateMenuFrame(self, nameOfNewMenuFrame):
        self.menuFrame.destroy()
        self.menuFrame=nameOfNewMenuFrame(self)
        self.menuFrame.grid(row=0,column=0,sticky=tkinter.W)

    def populateDisplayFrame(self, nameOfNewDisplayFrame):
        self.displayFrame.destroy()
        self.displayFrame=nameOfNewDisplayFrame(self)
        self.displayFrame.grid(row=1,column=0)

    def populateDisplayFrameWithLevelFrame(self, nameOfNewMenuFrame):
        self.displayFrame.destroy()
        self.displayFrame=LevelFrame(self,nameOfNewMenuFrame)
        self.displayFrame.grid(row=1,column=0,sticky=tkinter.W)

class MenuFrame(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A frame that holds a collection of buttons that, when pressed, change the displayFrame in the levelFrame
        """
        self.grid(row=0,column=0)

class DisplayFrame(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A frame that holds a collection of widgets that make up the information that needs to be displayed to the user
        """
        self.grid(row=0,column=0)

class TopMenuFrame(MenuFrame):
    def __init__(self, master):
        MenuFrame.__init__(self, master)
        """
        A collection of buttons that are used to navigate top-level menus
        """

        # Top-level menu buttons
        self.mainMenuButton=tkinter.Button(self, text="Main Menu", command=lambda : master.populateDisplayFrame(MainMenuDisplay))
        self.mainMenuButton.grid(row=0,column=0,sticky=tkinter.W)

        self.reportButton=tkinter.Button(self, text="Report", command=lambda : master.populateDisplayFrame(ReportDisplay))
        self.reportButton.grid(row=0,column=1,sticky=tkinter.W)

        self.mapButton=tkinter.Button(self, text="Map", command=lambda : master.populateDisplayFrameWithLevelFrame(MapMenuFrame))
        self.mapButton.grid(row=0,column=2,sticky=tkinter.W)

        self.approvalButton=tkinter.Button(self, text="Approval", command=lambda : master.populateDisplayFrame(ApprovalDisplay))
        self.approvalButton.grid(row=0,column=3,sticky=tkinter.W)

        self.destroyButton=tkinter.Button(self, text="Destroy Display Frame", command=lambda : master.displayFrame.destroy())
        self.destroyButton.grid(row=0,column=3,sticky=tkinter.W)

        self.mainMenuButton.invoke()

class MainMenuDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of buttons that comprise the main menu
        """

        # New game button
        self.newGameButton = tkinter.Button(self, text="New Game", command=lambda : saveload.newGame())
        self.newGameButton.grid(row=0,column=0)
        
        # Load game button
        self.loadGameButton = tkinter.Button(self, text="Load Game", command=lambda : master.populateDisplayFrame(LoadMenuDisplay))
        self.loadGameButton.grid(row=1,column=0)

        # Options button
        self.optionsButton = tkinter.Button(self, text="Options", command=lambda : master.populateDisplayFrameWithLevelFrame(OptionsMenuFrame))
        self.optionsButton.grid(row=2,column=0)

        # Quit button
        self.quitButton = tkinter.Button(self, text="Quit", command=window.destroy)
        self.quitButton.grid(row=3,column=0)

class LoadMenuDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of widgets that each display a saved gamestate and allow the user to load that gamestate
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

class OptionsMenuFrame(MenuFrame):
    def __init__(self, master):
        MenuFrame.__init__(self, master)
        """
        A collection of buttons that are used to navigate game, visual, and audio options menus
        """

        # Top-level menu buttons
        self.gameOptionsButton=tkinter.Button(self, text="Gameplay", command=lambda : master.populateDisplayFrame(GameOptionsDisplay))
        self.gameOptionsButton.grid(row=0,column=0,sticky=tkinter.W)

        self.visualOptionsButton=tkinter.Button(self, text="Visuals", command=lambda : master.populateDisplayFrame(VisualOptionsDisplay))
        self.visualOptionsButton.grid(row=0,column=1,sticky=tkinter.W)

        self.audioOptionsButton=tkinter.Button(self, text="Audio", command=lambda : master.populateDisplayFrame(AudioOptionsDisplay))
        self.audioOptionsButton.grid(row=0,column=2,sticky=tkinter.W)

        self.gameOptionsButton.invoke()

class GameOptionsDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of widgets that set and display game options
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

class VisualOptionsDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of widgets that set and display visual options
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

class AudioOptionsDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of widgets that set and display audio options
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

class ReportDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        Shows the results of missions
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

class MapMenuFrame(MenuFrame):
    def __init__(self, master):
        MenuFrame.__init__(self, master)
        """
        Shows the world map so that users can navigate missions by region
        """

        # A button should exist for each region
        for eachRegion in currentstate.gamestate.world.regions.values():
            self.label = tkinter.Label(self,text=eachRegion.name)
            self.label.grid()

class ApprovalDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        Shows the queued and pending missions the user has selected
        """

        self.label = tkinter.Label(self,text="Test "+self._name+str(master))
        self.label.grid()

# The window serves as a driver because it is an event listener
# Create the window that the game will run in
window=tkinter.Tk()
# What the program will display as
window.title("Test Window")
# Makes the window not fullscreen
window.attributes('-fullscreen',False)

# The top-level levelFrame is created, added to the window, and is given the top-level menu buttons
topLevel=LevelFrame(window,TopMenuFrame)

window.mainloop()