from Tkinter import *
import RPi.GPIO as GPIO

# Frame class
class MatchPuzzle(Frame):
    # Frame has a master, two images, and the light pins
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        # Create and resize the images, initialize the list of pins for lights
        self.img = PhotoImage(file = "black.gif")
        self.img = self.img.subsample(11)
        self.img2 = PhotoImage(file = "star.gif")
        self.img2 = self.img2.subsample(2)
        self.lights = [26, 13, 5, 27, 19, 6, 22, 21, 16, 24, 18, 20, 12, 23]
        
            
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
        # The numbered buttons switch the images of their respective
        # labels and turn on/off their corresponding LEDs
        b1 = Button(self.master, text = "1", padx = 10, pady = 5,\
                    command = lambda: self.callback(l1, self.lights[0]))
        b1.grid(row = 1, column = 0)

        b2 = Button(self.master, text = "2", padx = 10, pady = 5, \
                    command = lambda: self.callback(l2, self.lights[1]))
        b2.grid(row = 1, column = 2)

        b3 = Button(self.master, text = "3", padx = 10, pady = 5, \
                    command = lambda: self.callback(l3, self.lights[2]))
        b3.grid(row = 1, column = 4)

        b4 = Button(self.master, text = "4", padx = 10, pady = 5,\
                    command = lambda: self.callback(l4, self.lights[3]))
        b4.grid(row = 1, column = 6)

        b5 = Button(self.master, text = "5", padx = 10, pady = 5,\
                    command = lambda: self.callback(l5, self.lights[4]))
        b5.grid(row = 3, column = 1)

        b6 = Button(self.master, text = "6", padx = 10, pady = 5,\
                    command = lambda: self.callback(l6, self.lights[5]))
        b6.grid(row = 3, column = 3)

        b7 = Button(self.master, text = "7", padx = 10, pady = 5,\
                    command = lambda: self.callback(l7, self.lights[6]))
        b7.grid(row = 3, column = 5)

        b8 = Button(self.master, text = "8", padx = 10, pady = 5,\
                    command = lambda: self.callback(l8, self.lights[7]))
        b8.grid(row = 5, column = 0)

        b9 = Button(self.master, text = "9", padx = 10, pady = 5,\
                    command = lambda: self.callback(l9, self.lights[8]))
        b9.grid(row = 5, column = 2)

        b10 = Button(self.master, text = "10", padx = 10, pady = 5,\
                     command = lambda: self.callback(l10, self.lights[9]))
        b10.grid(row = 5, column = 4)

        b11 = Button(self.master, text = "11", padx = 10, pady = 5,
                     command = lambda: self.callback(l11, self.lights[10]))
        b11.grid(row = 5, column = 6)

        b12 = Button(self.master, text = "12", padx = 10, pady = 5,\
                     command = lambda: self.callback(l12, self.lights[11]))
        b12.grid(row = 7, column = 1)

        b13 = Button(self.master, text = "13", padx = 10, pady = 5,\
                     command = lambda: self.callback(l13, self.lights[12]))
        b13.grid(row = 7, column = 3)

        b14 = Button(self.master, text = "14", padx = 10, pady = 5,\
                     command = lambda: self.callback(l14, self.lights[13]))
        b14.grid(row = 7, column = 5)

        # The finish button checks to see if the right lighst are lit
        # and calls the win function
        f = Button(self.master, text = "Finish", padx = 10, pady = 5,\
                     command = self.finish)
        f.grid(row = 8, column = 3)

        # This label returns the user/password fr the puzzle upon completion
        # of the game
        MatchPuzzle.result = Label(self.master, bg = "black", fg = "yellow",\
                                   text = "Create your constellation.")
        MatchPuzzle.result.grid(row = 10, column = 0, columnspan = 7, sticky = N+S+E+W)


    # Command for the button
    # Switches images and turns LEDs on/off
    def callback(self, label, pin):
        if (label.image == self.img):
            label.configure(image = self.img2)
            label.image = self.img2

        elif (label.image == self.img2):
            label.configure(image = self.img)
            label.image = self.img
        
        if (GPIO.input(pin) == 0):
            GPIO.output(pin, True)
            
        else:
            GPIO.output(pin, False)

    # Finish button command
    # Checks if the constellation is correct depending
    # on what the team picked from the dropdown menu
    # (I assume we're using a global variable for it)
    def finish(self):
        if (constellation == "Phoenix"):
            finish = [19, 6, 22, 21, 16, 24, 18, 12]

        elif (constellation == "Taurus"):
            finish = [26, 13, 19, 6, 22, 24, 18, 23]

        elif (constellation == "Canis Major"):
            finish = [13, 27, 19, 6, 22, 20, 12, 23]

        elif (constellation == "Canes Venatici"):
            finish = [22, 20]

        elif (constellation == "Chameleon"):
            finish = [6, 22, 21, 24, 12]

        elif (constellation == "Crater"):
            finish = [13, 5, 19, 16, 24, 18, 20, 23]

        elif (constellation == "Draco"):
            finish = [13, 5, 22, 21, 16, 24, 20, 23]

        elif (constellation == "Vulpecula"):
            finish = [26, 19, 21, 16, 24, 23]
        
        if (all(GPIO.input(pin) for pin in finish) == 1):
            self.win()

        else:
            self.fail()

    # Sets up the GPIO functions
    def setupGPIO(self):

       GPIO.setmode(GPIO.BCM)

       for pin in self.lights:
           GPIO.setup(pin, GPIO.OUT)
           GPIO.output(pin, False)

    # Returns the needed user/password combo and cleans the pins
    def win(self):
        MatchPuzzle.result.config(text = "user/password || Canvas Data")
        GPIO.cleanup()

    def fail(self):
        MatchPuzzle.result.config(text = "Try Again.")

    # plays the game
    def play(self):
        self.setupGUI()
        self.setupGPIO()

# Cleans GPIO pins if window closes      
def onClose():
    GPIO.cleanup()
    window.destroy()        
        
# Main part of program
# Create window, assign frame to it, play the game, and run the window

#Result from the drop down box (change to fit as needed)
global constellation
constellation = "Taurus"


window = Tk()
window.configure(bg = "black")
window.title("Match Game")
t = MatchPuzzle(window)
t.play()
window.protocol("WM_DELETE_WINDOW", onClose)
window.mainloop()

