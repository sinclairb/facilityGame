import tkinter

class frameWithRemoveMethod(tkinter.Frame):
    def __init__(self,*x):
        tkinter.Frame.__init__(self,*x)
        self.pack()

    def removethis(self):
        for child in self.winfo_children():
            child.destroy()
        self.destroy()

class GUI1(frameWithRemoveMethod):
    def __init__(self):
        frameWithRemoveMethod.__init__(self)
        self.label = tkinter.Label(self, text="This is GUI1")
        self.label.pack()
        self.button = tkinter.Button(self, text="Destroy Everything", command=self.removethis)
        self.button.pack()
        
        self.internalFrame = GUI2(self)
        self.internalFrame.pack()
    
class GUI2(frameWithRemoveMethod):
    def __init__(self,x):
        frameWithRemoveMethod.__init__(self,x)
        self.label = tkinter.Label(self, text="This is GUI2")
        self.label.pack()
        



window = tkinter.Tk()
GUI1()
window.mainloop()