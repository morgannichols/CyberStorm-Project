# Button switch puzzle

import RPi.GPIO as GPIO
from Tkinter import *


# Frame for the puzzle
# Has the pin values for all the LEDs
class LightPuzzle(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.lights = [26, 13, 5, 27, 19, 6, 22, 21, 16, 24, 18, 20, 12, 23]

    # Sets up puzzle for Phoenix constellation
    def setupPhoenixGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.switch(self.lights[0], self.lights[4]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.switch(self.lights[1], self.lights[8]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.switch(self.lights[2], self.lights[9]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[3], self.lights[10]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.switch(self.lights[7], self.lights[11]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.double(self.lights[5], self.lights[12]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[6], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for Taurus constellation
    def setupTaurusGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.switch(self.lights[0], self.lights[7]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.switch(self.lights[1], self.lights[8]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.switch(self.lights[2], self.lights[9]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[3], self.lights[10]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.switch(self.lights[4], self.lights[11]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.double(self.lights[5], self.lights[6]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[12], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for Canis Major constellation
    def setupCanisMajorGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.switch(self.lights[0], self.lights[1]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.double(self.lights[4], self.lights[5]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.double(self.lights[6], self.lights[12]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[2], self.lights[3]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.double(self.lights[7], self.lights[8]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.switch(self.lights[9], self.lights[11]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[10], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for the Canes Venatici constellation
    def setupCanesVenaticiGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.double(self.lights[0], self.lights[8]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.double(self.lights[1], self.lights[12]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.double(self.lights[2], self.lights[7]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[3], self.lights[6]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.switch(self.lights[5], self.lights[11]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.double(self.lights[4], self.lights[10]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[9], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for the Chameleon constellation
    def setupChameleonGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.double(self.lights[0], self.lights[4]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.switch(self.lights[1], self.lights[7]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.switch(self.lights[2], self.lights[5]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[3], self.lights[6]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.double(self.lights[9], self.lights[12]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.double(self.lights[8], self.lights[11]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.double(self.lights[10], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for the Draco constellation
    def setupDracoGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.switch(self.lights[0], self.lights[7]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.switch(self.lights[1], self.lights[3]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.double(self.lights[2], self.lights[8]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[5], self.lights[11]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.switch(self.lights[6], self.lights[12]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.switch(self.lights[9], self.lights[10]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[4], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for the Crater constellation
    def setupCraterGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.double(self.lights[0], self.lights[3]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.double(self.lights[4], self.lights[8]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.double(self.lights[1], self.lights[2]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.double(self.lights[6], self.lights[9]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.double(self.lights[7], self.lights[11]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.double(self.lights[5], self.lights[12]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.double(self.lights[10], self.lights[13]))
        b7.grid(row = 1, column = 5)

        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # Sets up puzzle for the Vulpecula constellation
    def setupVulpeculaGUI(self):
        
        b1 = Button(self.master, text = "Group 1",\
                    command = lambda: self.switch(self.lights[0], self.lights[2]))
        b1.grid(row = 0, column = 0)
        
        b2 = Button(self.master, text = "Group 2",\
                    command = lambda: self.double(self.lights[1], self.lights[5]))
        b2.grid(row = 0, column = 2)
        
        b3 = Button(self.master, text = "Group 3",\
                    command = lambda: self.switch(self.lights[3], self.lights[4]))
        b3.grid(row = 0, column = 4)
        
        b4 = Button(self.master, text = "Group 4",\
                    command = lambda: self.switch(self.lights[6], self.lights[9]))
        b4.grid(row = 0, column = 6)
        
        b5 = Button(self.master, text = "Group 5",\
                    command = lambda: self.switch(self.lights[7], self.lights[11]))
        b5.grid(row = 1, column = 1)

        b6 = Button(self.master, text = "Group 6",\
                    command = lambda: self.switch(self.lights[8], self.lights[12]))
        b6.grid(row = 1, column = 3)
        
        b7 = Button(self.master, text = "Group 7",\
                    command = lambda: self.switch(self.lights[10], self.lights[13]))
        b7.grid(row = 1, column = 5)
            
        lf = Label(self.master, bg = "black")
        lf.grid(row = 2, column = 3)

        f = Button(self.master, text = "Finish", command = self.finish)
        f.grid(row = 3, column = 3)

        LightPuzzle.result = Label(self.master, bg = "black", fg = "yellow")
        LightPuzzle.result.grid(row = 4, column = 0, columnspan = 7, sticky = N+S+E+W)

    # One of the button commands
    # Turns one light off and turns another on   
    def switch(self, pin1, pin2):
        if (GPIO.input(pin1) == 1):
            GPIO.output(pin1, False)
            GPIO.output(pin2, True)
        else:
            GPIO.output(pin1, True)
            GPIO.output(pin2, False)

    # One of the button commands
    # Turns two lights on and off simultaneously
    def double(self, pin1, pin2):
        if (GPIO.input(pin1) == 1 and GPIO.input(pin2) == 1):
            GPIO.output(pin1, False)
            GPIO.output(pin2, False)

        elif (GPIO.input(pin1) == 0 and GPIO.input(pin2) == 0):
            GPIO.output(pin1, True)
            GPIO.output(pin2, True)

    # Command for the finish button
    def finish(self):

        # Sets the win condition depending
        # on which constellation the puzzle
        # is about
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
            
        # If all the live pins meet the condition the player wins
        if (all(GPIO.input(pin) for pin in finish) == 1):
            self.win()
            
    # Sets the GPIO
    def setupGPIO(self):
        
        GPIO.setmode(GPIO.BCM)

        # Determines which LEDs start turned on
        # when the puzzle begins based on which constellation
        # was chosen from the drop-down menu
        if (constellation == "Phoenix"):
            start = [13, 27, 19, 24, 20, 23]

        elif (constellation == "Taurus"):
            start = [5, 27, 21, 16, 20, 12]

        elif (constellation == "Canis Major"):
            start = [26, 5, 19, 6, 24, 23]

        elif (constellation == "Canes Venatici"):
            start = [26, 13, 19, 22, 24, 16, 18, 20, 12, 23]

        elif (constellation == "Chameleon"):
            start = [26, 13, 5, 27, 19, 16, 24, 18, 20, 12, 23]

        elif (constellation == "Crater"):
            start = []

        elif (constellation == "Draco"):
            start = [26, 27, 19, 6, 22, 18]

        elif (constellation == "Vulpecula"):
            start = [13, 5, 27, 16, 6, 22, 21, 18]
        

        for pin in self.lights:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        GPIO.output(start, True)

            
    def win(self):
        # Feeds the player the user/password data to complete the puzzle
        # and part of the phrase needed to complete the Constellation Canvas
        LightPuzzle.result.config(text = "user/password || Canvas Data")
        GPIO.cleanup()

    # Plays the light switch game
    # Sets up a specific constellation puzzle
    # depending on the drop-down menu option
    def play(self):
        if (constellation == "Phoenix"):
            self.setupPhoenixGUI()

        elif (constellation == "Taurus"):
            self.setupTaurusGUI()

        elif (constellation == "Canis Major"):
            self.setupCanisMajorGUI()

        elif (constellation == "Canes Venatici"):
            self.setupCanesVenaticiGUI()

        elif (constellation == "Chameleon"):
            self.setupChameleonGUI()

        elif (constellation == "Draco"):
            self.setupDracoGUI()

        elif (constellation == "Crater"):
            self.setupCraterGUI()

        elif (constellation == "Vulpecula"):
            self.setupVulpeculaGUI()
            
        self.setupGPIO()
        
# Cleans the pins if the window is closed
def onClose():
    GPIO.cleanup()
    window.destroy()
        
# main part of program

# Drop down menu option
global constellation
constellation = "Vulpecula"

# Create the window and setup the game
window = Tk()
window.config(bg = "black")
t = LightPuzzle(window)
t.play()
window.protocol("WM_DELETE_WINDOW", onClose)
window.mainloop()

