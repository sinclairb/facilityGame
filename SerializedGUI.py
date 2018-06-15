import tkinter
import currentstate
import saveload

class LevelFrame(tkinter.Frame):
    def __init__(self, master, nameOfMenuFrame=None, region=None):
        tkinter.Frame.__init__(self, master)
        """
        A collection of frames/widgets that are added to the frame passed as the "master" parameter
        A levelFrame consists of a frame that holds menu buttons, and a frame that displays info
        """
        self.grid(row=0,column=0)

        # Creates an attribute that contains the region (if any) that was passed to the levelFrame
        self.region=region

        # A frame that holds menu buttons
        self.menuFrame=MenuFrame(self)
        self.menuFrame.grid(row=0,column=0)

        # A frame that holds whatever info should be displayed based on which button in the menuFame was pressed
        # Initialized to an empty frame, but populated via the populateDisplayFrame method
        self.displayFrame=DisplayFrame(self)
        self.displayFrame.grid(row=1,column=0)

        # Creates a menu frame of the specified type, if one is specified
        if nameOfMenuFrame:
            self.populateMenuFrame(nameOfMenuFrame, region)

    def populateMenuFrame(self, nameOfNewMenuFrame, region=None):
        self.menuFrame.destroy()
        # Checks if a region is passed to the levelFrame. If one is, that means that a MissionsMenuFrame should be created for that region
        if region:
            self.menuFrame=MissionsMenuFrame(self, region)
        else:
            self.menuFrame=nameOfNewMenuFrame(self)
        self.menuFrame.grid(row=0,column=0,sticky=tkinter.W)

    def populateDisplayFrame(self, nameOfNewDisplayFrame):
        self.displayFrame.destroy()
        self.displayFrame=nameOfNewDisplayFrame(self)
        self.displayFrame.grid(row=1,column=0)

    def populateDisplayFrameWithLevelFrame(self, nameOfNewMenuFrame, region=None):
        self.displayFrame.destroy()
        self.displayFrame=LevelFrame(self,nameOfNewMenuFrame,region)
        self.displayFrame.grid(row=1,column=0,sticky=tkinter.W)

    def populateMissionsMenuFrame(self, region):
        self.menuFrame.destroy()
        self.menuFrame=MissionsMenuFrame(self, region)
        self.menuFrame.grid(row=0,column=0,sticky=tkinter.W)

class MenuFrame(tkinter.Frame):
    def __init__(self, master, region=None):
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

        if currentstate.gamestate:
            self.reportButton=tkinter.Button(self, text="Report", command=lambda : master.populateDisplayFrame(ReportDisplay))
            self.reportButton.grid(row=0,column=1,sticky=tkinter.W)

            self.mapButton=tkinter.Button(self, text="Map", command=lambda : master.populateDisplayFrameWithLevelFrame(MapMenuFrame))
            self.mapButton.grid(row=0,column=2,sticky=tkinter.W)

            self.approvalButton=tkinter.Button(self, text="Approval", command=lambda : master.populateDisplayFrame(ApprovalDisplay))
            self.approvalButton.grid(row=0,column=3,sticky=tkinter.W)

            self.destroyButton=tkinter.Button(self, text="Destroy Display Frame", command=lambda : master.displayFrame.destroy())
            self.destroyButton.grid(row=0,column=4,sticky=tkinter.W)

        self.mainMenuButton.invoke()

class MainMenuDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        A collection of buttons that comprise the main menu
        """

        # New game button
        self.newGameButton = tkinter.Button(self, text="New Game", command=lambda : [saveload.newGame(),master.populateMenuFrame(TopMenuFrame)])
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

        self.baseButton=tkinter.Button(self, text="Base", command=lambda : master.populateDisplayFrameWithLevelFrame(MissionsMenuFrame, currentstate.gamestate.world.facility))
        self.baseButton.grid(row=0, column=0)

        # A menu button should exist for each region, which displays the region's missions menu
        self.regionButtons=[]
        for index, aRegion in enumerate(currentstate.gamestate.world.regions):
            self.regionButtons.append(tkinter.Button(self, text=aRegion.name, command=lambda aRegion=aRegion: master.populateDisplayFrameWithLevelFrame(MissionsMenuFrame, aRegion)))
            self.regionButtons[index].grid(row=0,column=index+1)


        self.baseButton.invoke()

class MissionsMenuFrame(MenuFrame):
    def __init__(self, master, region):
        MenuFrame.__init__(self, master)
        """
        A collection of buttons that allow the user to navigate between the base overview and mission types
        """
        self.overviewButton=tkinter.Button(self, text="Overview", command=lambda : master.populateDisplayFrame(RegionOverviewDisplay))
        self.overviewButton.grid(row=0, column=0)

        


        self.overviewButton.invoke()

class RegionOverviewDisplay(DisplayFrame):
    def __init__(self, master):
        DisplayFrame.__init__(self, master)
        """
        Shows the overview of the base
        """
        self.region=master.region

        self.label = tkinter.Label(self,text=str(self.region)+self.region.name+" Test "+self._name+str(master))
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