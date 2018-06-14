import tkinter

class levelFrame(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A collection of frames/widgets that are added to the frame passed as the "master" parameter
        A levelFrame consists of a frame that holds menu buttons, and a frame that displays info
        """
        self.grid(row=0,column=0)

        # A frame that holds menu buttons
        self.menuFrame=menuFrame(self)
        self.menuFrame.grid(row=0,column=0)

        # A frame that holds whatever info should be displayed based on which button in the menuFame was pressed
        # Initialized to an empty frame, but populated via the populateDisplayFrame method
        self.displayFrame=displayFrame(self)
        self.displayFrame.grid(row=1,column=0)

    def populateDisplayFrame(self, nameOfNewDisplayFrame):
        print("populate",nameOfNewDisplayFrame)
        self.displayFrame.destroy()
        self.displayFrame=nameOfNewDisplayFrame(self)
        self.displayFrame.grid(row=1,column=0)

class menuFrame(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A frame that holds a collection of buttons that, when pressed, change the displayFrame in the levelFrame
        Buttons should be named button1, button2, etc. so that they can easily be referenced from other places in the code
        """
        self.grid(row=0,column=0)

        self.button1=tkinter.Button(self, text="Test Menu", command=lambda : master.populateDisplayFrame(displayFrame))
        self.button1.grid(row=0,column=0,sticky=tkinter.W)

class displayFrame(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A frame that holds a collection of widgets that make up the information that needs to be displayed to the user
        """
        self.grid(row=0,column=0)

        self.la = tkinter.Label(self,text="Test Display"+str(master))
        self.la.grid()

class topMenuFrame(menuFrame):
    def __init__(self, master):
        menuFrame.__init__(self, master)
        """
        A collection of buttons that are used to navigate top-level menus
        """

        # Top-level menu buttons
        self.button1=tkinter.Button(self, text="Main Menu", command=lambda : master.populateDisplayFrame(mainMenuDisplay))
        self.button1.grid(row=0,column=0,sticky=tkinter.W)

        self.button2=tkinter.Button(self, text="Report")
        self.button2.grid(row=0,column=1,sticky=tkinter.W)

        self.button3=tkinter.Button(self, text="Map")
        self.button3.grid(row=0,column=2,sticky=tkinter.W)

        self.button4=tkinter.Button(self, text="Approval")
        self.button4.grid(row=0,column=3,sticky=tkinter.W)

class mainMenuDisplay(displayFrame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        """
        A collection of buttons that comprise the main menu
        """

        # Quit button
        self.quitButton = tkinter.Button(self, text="Quit", command=window.destroy)
        self.quitButton.pack()

# The window serves as a driver because it is an event listener
# Create the window that the game will run in
window=tkinter.Tk()
# What the program will display as
window.title("Test Window")
# Makes the window fullscreen
window.attributes('-fullscreen',False)

# The top-level levelFrame is created, added to the window, and is given the top-level menu buttons
topLevel=levelFrame(window)
topMenu=menuFrame(topLevel)

window.mainloop()