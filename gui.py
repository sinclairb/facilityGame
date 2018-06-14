import tkinter
import currentstate
import saveload


class menuFrame(tkinter.Frame):
    def __init__(self,*master):
        tkinter.Frame.__init__(self,*master)
        self.pack()

    def switchTo(self, newMenuFrame):
        """
        Creates a new frame of the newMenuFrame parameter type, and destroys itself
        """
        newMenuFrame()
        self.destroy()



class mainMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Allows the user to create a new game, load a game, save a game, change game and window options, and quit
        """
        # Menu label
        self.mainMenuLabel = tkinter.Label(self,text="Main Menu")
        self.mainMenuLabel.pack()

        # If a game has been loaded, the user can play it
        if currentstate.gamestate!=None:
            # Play game button
            self.reportButton = tkinter.Button(self, text="Back to Game", command=lambda : self.switchTo(reportMenu))
            self.reportButton.pack()

        # New game button
        self.newGameButton = tkinter.Button(self, text="New Game", command=lambda : [saveload.newGame(),self.switchTo(reportMenu)])
        self.newGameButton.pack()
        
        # Load game button
        self.loadGameButton = tkinter.Button(self, text="Load Game", command=lambda : self.switchTo(loadMenu))
        self.loadGameButton.pack()

        # Options button
        self.optionsButton = tkinter.Button(self, text="Options", command=lambda : self.switchTo(optionsMenu))
        self.optionsButton.pack()

        # Quit button
        self.quitButton = tkinter.Button(self, text="Quit", command=window.destroy)
        self.quitButton.pack()
        


class loadMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Displays the user's save games, and allows them to load save games
        """
        # Menu label
        self.loadMenuLabel = tkinter.Label(self,text="Load Menu")
        self.loadMenuLabel.pack()

        # Back to mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Back to Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()

        # Display save games
        selected=""
        
        # Load selected save game
        self.loadSaveButton = tkinter.Button(self, text="Load Selected Save", command= lambda: saveload.loadGame(selected))
        self.loadSaveButton.pack()



class optionsMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Allows the user to view and change game options and window options
        """
        # Menu label
        self.optionsMenuLabel = tkinter.Label(self,text="Options Menu")
        self.optionsMenuLabel.pack()

        # Back to mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Back to Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()
        
        # Fullscreen toggle
        self.fullscreenButton = tkinter.Button(self, text="Toggle Fullscreen", command= lambda: window.attributes('-fullscreen', (not window.attributes('-fullscreen'))))
        self.fullscreenButton.pack()



class reportMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Displays the results of the previous turn's missions
        """
        # Menu label
        self.reportMenuLabel = tkinter.Label(self,text="Report Menu")
        self.reportMenuLabel.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Main Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()

        # mapMenu button
        self.mapMenuButton = tkinter.Button(self, text="Map Menu", command=lambda : self.switchTo(mapMenu))
        self.mapMenuButton.pack()

        # approvalMenu button
        self.approvalMenuButton = tkinter.Button(self, text="Approval Menu", command=lambda : self.switchTo(approvalMenu))
        self.approvalMenuButton.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Funds display
        self.fundsLabel = tkinter.Label(self,text="Funds: "+format(currentstate.gamestate.funds,","))
        self.fundsLabel.pack()

        # Week display
        self.weekLabel = tkinter.Label(self,text="Week: "+str(currentstate.gamestate.week))
        self.weekLabel.pack()

        # If it's the first turn, display customization and intro/tutorial
        if currentstate.gamestate.week==0:
            # Name display
            self.playerNameCustomizationFrame = nameChangeFrame(currentstate.gamestate.player, self)
            self.playerNameCustomizationFrame.pack()



class nameChangeFrame(menuFrame):
    def __init__(self,passedCharacter,*master):
        menuFrame.__init__(self,*master)
        """
        Displays the first and last name of the passedCharacter, along with a button that updates the name
        """
        self.firstNameEntry = tkinter.Entry(self)
        self.firstNameEntry.insert(0,passedCharacter.firstName)
        self.firstNameEntry.pack()

        self.lastNameEntry = tkinter.Entry(self)
        self.lastNameEntry.insert(0,passedCharacter.lastName)
        self.lastNameEntry.pack()

        self.updateNameButton = tkinter.Button(self, text="Update Name", command=lambda : [self.updateName(passedCharacter)])
        self.updateNameButton.pack()

    def updateName(self, passedCharacter):
        passedCharacter.firstName=self.firstNameEntry.get()
        passedCharacter.lastName=self.lastNameEntry.get()

        

class mapMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Displays the world map
        """
        # Menu label
        self.mapMenuLabel = tkinter.Label(self,text="Map Menu")
        self.mapMenuLabel.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Main Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()

        # reportMenu button
        self.reportMenuButton = tkinter.Button(self, text="Report Menu", command=lambda : self.switchTo(reportMenu))
        self.reportMenuButton.pack()

        # approvalMenu button
        self.approvalMenuButton = tkinter.Button(self, text="Approval Menu", command=lambda : self.switchTo(approvalMenu))
        self.approvalMenuButton.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Funds display
        self.fundsLabel = tkinter.Label(self,text="Funds: "+format(currentstate.gamestate.funds,","))
        self.fundsLabel.pack()

        # Heat display
        self.heatLabel = tkinter.Label(self,text="Heat: "+str(currentstate.gamestate.globalHeat))
        self.heatLabel.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        # baseMenu button
        self.baseMenuButton = tkinter.Button(self, text="Base", command=lambda : self.switchTo(baseMenu))
        self.baseMenuButton.pack()

        # Menu buttons for each region
        #self.northAmericaMenuButton = tkinter.Button(self, text="North America", command=lambda : self.switchTo(northAmericaMenu))
        #self.northAmericaMenuButton.pack()

        #self.southAmericaMenuButton = tkinter.Button(self, text="South America", command=lambda : self.switchTo(southAmericaMenu))
        #self.southAmericaMenuButton.pack()

        #self.europeMenuButton = tkinter.Button(self, text="Europe", command=lambda : self.switchTo(europeMenu))
        #self.europeMenuButton.pack()

        #self.asiaMenuButton = tkinter.Button(self, text="Asia", command=lambda : self.switchTo(asiaMenu))
        #self.asiaMenuButton.pack()

        #self.africaMenuButton = tkinter.Button(self, text="Africa", command=lambda : self.switchTo(africaMenu))
        #self.africaMenuButton.pack()

        #self.australiaMenuButton = tkinter.Button(self, text="Australia", command=lambda : self.switchTo(australiaMenu))
        #self.australiaMenuButton.pack()



class baseMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Displays the base overview and the roster and base missions buttons
        """
        # Menu label
        self.baseMenuLabel = tkinter.Label(self,text="Base Menu")
        self.baseMenuLabel.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Main Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()

        # reportMenu button
        self.reportMenuButton = tkinter.Button(self, text="Report Menu", command=lambda : self.switchTo(reportMenu))
        self.reportMenuButton.pack()

        # mapMenu button
        self.mapMenuButton = tkinter.Button(self, text="Map Menu", command=lambda : self.switchTo(mapMenu))
        self.mapMenuButton.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Base overview
        

        # Roster button

        # Missions Button


class approvalMenu(menuFrame):
    def __init__(self):
        menuFrame.__init__(self)
        """
        Displays an overview of all current missions
        """
        # Menu label
        self.approvalMenuLabel = tkinter.Label(self,text="Approval Menu")
        self.approvalMenuLabel.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # mainMenu button
        self.backToMainMenuButton = tkinter.Button(self, text="Main Menu", command=lambda : self.switchTo(mainMenu))
        self.backToMainMenuButton.pack()

        # reportMenu button
        self.reportMenuButton = tkinter.Button(self, text="Report Menu", command=lambda : self.switchTo(reportMenu))
        self.reportMenuButton.pack()

        # mapMenu button
        self.mapMenuButton = tkinter.Button(self, text="Map Menu", command=lambda : self.switchTo(mapMenu))
        self.mapMenuButton.pack()

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # nextTurn button
        self.nextTurnButton = tkinter.Button(self, text="Finalize Orders", command=lambda : [nextTurn(), self.switchTo(reportMenu)])
        self.nextTurnButton.pack()



def nextTurn():
    """
    Processes all orders, simulates events, updates values, arrives at mission outcomes, saves the game
    """
    # Do everything, then increase week and save
    currentstate.gamestate.week+=1
    saveload.saveGame()




# The window serves as a driver because it is an event listener
# Create the window that the game will run in
window=tkinter.Tk()
# What the program will display as
window.title("Facility Game")
# Makes the window fullscreen
window.attributes('-fullscreen',False)
# Displays the main menu
mainMenu()
window.mainloop()
    