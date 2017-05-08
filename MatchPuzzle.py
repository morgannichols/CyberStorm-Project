from Tkinter import *

# Frame class
class MatchPuzzle(Frame):
    # Frame has a master and two images
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        # Create and resize the images
        self.img = PhotoImage(file = "black.gif")
        self.img = self.img.subsample(11)
        self.img2 = PhotoImage(file = "star.gif")
        self.img2 = self.img2.subsample(2)

    # Command for the button       
    def callback(self, label):
        if (label.image == self.img):
            label.configure(image = self.img2)
            label.image = self.img2

        elif (label.image == self.img2):
            label.configure(image = self.img)
            label.image = self.img
            
    # Create GUI elements    
    def setupGUI(self):
        
        # Create the labels
        l1 = Label(self.master, image = self.img)
        l1.image = self.img
        l1.grid(row = 0, column = 0)

        l2 = Label(self.master, image = self.img)
        l2.image = self.img
        l2.grid(row = 0, column = 2)

        l3 = Label(self.master, image = self.img)
        l3.image = self.img
        l3.grid(row = 0, column = 4)

        l4 = Label(self.master, image = self.img)
        l4.image = self.img
        l4.grid(row = 0, column = 6)

        l5 = Label(self.master, image = self.img)
        l5.image = self.img
        l5.grid(row = 2, column = 1)

        l6 = Label(self.master, image = self.img)
        l6.image = self.img
        l6.grid(row = 2, column = 3)

        l7 = Label(self.master, image = self.img)
        l7.image = self.img
        l7.grid(row = 2, column = 5)

        l8 = Label(self.master, image = self.img)
        l8.image = self.img
        l8.grid(row = 4, column = 0)

        l9 = Label(self.master, image = self.img)
        l9.image = self.img
        l9.grid(row = 4, column = 2)

        l10 = Label(self.master, image = self.img)
        l10.image = self.img
        l10.grid(row = 4, column = 4)

        l11 = Label(self.master, image = self.img)
        l11.image = self.img
        l11.grid(row = 4, column = 6)

        l12 = Label(self.master, image = self.img)
        l12.image = self.img
        l12.grid(row = 6, column = 1)

        l13 = Label(self.master, image = self.img)
        l13.image = self.img
        l13.grid(row = 6, column = 3)

        l14 = Label(self.master, image = self.img)
        l14.image = self.img
        l14.grid(row = 6, column = 5)
        
        # Create the buttons
        b1 = Button(self.master, text = "1", padx = 10, pady = 5, command = lambda: self.callback(l1))
        b1.grid(row = 1, column = 0)

        b2 = Button(self.master, text = "2", padx = 10, pady = 5, command = lambda: self.callback(l2))
        b2.grid(row = 1, column = 2)

        b3 = Button(self.master, text = "3", padx = 10, pady = 5, command = lambda: self.callback(l3))
        b3.grid(row = 1, column = 4)

        b4 = Button(self.master, text = "4", padx = 10, pady = 5, command = lambda: self.callback(l4))
        b4.grid(row = 1, column = 6)

        b5 = Button(self.master, text = "5", padx = 10, pady = 5, command = lambda: self.callback(l5))
        b5.grid(row = 3, column = 1)

        b6 = Button(self.master, text = "6", padx = 10, pady = 5, command = lambda: self.callback(l6))
        b6.grid(row = 3, column = 3)

        b7 = Button(self.master, text = "7", padx = 10, pady = 5, command = lambda: self.callback(l7))
        b7.grid(row = 3, column = 5)

        b8 = Button(self.master, text = "8", padx = 10, pady = 5, command = lambda: self.callback(l8))
        b8.grid(row = 5, column = 0)

        b9 = Button(self.master, text = "9", padx = 10, pady = 5, command = lambda: self.callback(l9))
        b9.grid(row = 5, column = 2)

        b10 = Button(self.master, text = "10", padx = 10, pady = 5, command = lambda: self.callback(l10))
        b10.grid(row = 5, column = 4)

        b11 = Button(self.master, text = "11", padx = 10, pady = 5, command = lambda: self.callback(l11))
        b11.grid(row = 5, column = 6)

        b12 = Button(self.master, text = "12", padx = 10, pady = 5, command = lambda: self.callback(l12))
        b12.grid(row = 7, column = 1)

        b13 = Button(self.master, text = "13", padx = 10, pady = 5, command = lambda: self.callback(l13))
        b13.grid(row = 7, column = 3)

        b14 = Button(self.master, text = "14", padx = 10, pady = 5, command = lambda: self.callback(l14))
        b14.grid(row = 7, column = 5)
        
# Main part of program
# Create window, assign frame to it, setup the GUI, and run the window
window = Tk()
window.configure(bg = "black")
window.title("Match Game")
t = MatchPuzzle(window)
t.setupGUI()
window.mainloop()
