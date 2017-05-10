# Constellation Canvas

from Tkinter import *

# the 2D point class
class Point(object):
    # Point has an x-coordinate and a y-coordinate, set as floating points and defaulted to 0.0
    def __init__(self, x = 0.0, y = 0.0):
        self.x = float(x)
        self.y = float(y)

    # Getters and Setters
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # Calculates distance between two points
    def dist(self, point):
        x = (point.x - self.x)**2
        y = (point.y - self.y)**2
        z = x+y
        distance = math.sqrt(z)
        return distance

    # Finds the midpoint between two points
    def midpt(self, point):
        x = (point.x + self.x)/2
        y = (point.y + self.y)/2
        midpt = Point(x, y)
        return midpt

    # String representation of a point
    def __str__(self):
        return "({},{})".format(self.x,self.y)

# the Constellation class
# inherits from the Canvas class of Tkinter
class Constellation(Canvas):
    def __init__(self, master):
        # Initialize canvas, set background to white
        Canvas.__init__(self, master, bg = "black", highlightthickness = 0)
        
    # Plots points
    # Takes in point and color
    def plot(self, point):
        self.create_oval(point.x, point.y, point.x + POINT_RADIUS * 2, point.y + POINT_RADIUS * 2, outline = POINT_COLOR, fill = POINT_COLOR)

    # Plots line between points
    def drawLine(self, point, point2):
        self.create_line(point.x, point.y, point2.x, point2.y, fill = LINE_COLOR)

    # Plots Phoenix constellation
    def plotPhoenix(self):
        p1 = Point(315, 130)
        p2 = Point(190, 200)
        p3 = Point(350, 175)
        p4 = Point(190, 365)
        p5 = Point(260, 395)
        p6 = Point(120, 150)
        p7 = Point(120, 220)
        p8 = Point(440, 150)
        p9 = Point(365, 325)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)
        self.plot(p8)
        self.plot(p9)

        self.drawLine(p1, p2)
        self.drawLine(p1, p3)
        self.drawLine(p2, p4)
        self.drawLine(p3, p5)
        self.drawLine(p4, p5)
        self.drawLine(p2, p6)
        self.drawLine(p6, p7)
        self.drawLine(p3, p8)
        self.drawLine(p8, p9)

    # Plots Taurus constellation
    def plotTaurus(self):
        p1 = Point(205, 160)
        p2 = Point(180, 190)
        p3 = Point(290, 210)
        p4 = Point(290, 245)
        p5 = Point(310, 240)
        p6 = Point(312, 245)
        p7 = Point(313, 250)
        p8 = Point(305, 255)
        p9 = Point(330, 275)
        p10 = Point(400, 305)
        p11 = Point(400, 310)
        p12 = Point(320, 310)
        p13 = Point(350, 365)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)
        self.plot(p8)
        self.plot(p9)
        self.plot(p10)
        self.plot(p11)
        self.plot(p12)
        self.plot(p13)

        self.drawLine(p1, p3)
        self.drawLine(p2, p4)
        self.drawLine(p3, p5)
        self.drawLine(p5, p6)
        self.drawLine(p6, p7)
        self.drawLine(p4, p8)
        self.drawLine(p8, p9)
        self.drawLine(p9, p10)
        self.drawLine(p11, p12)
        self.drawLine(p11, p13)
        
    # Plot Canis Major constellation
    def plotCanisMajor(self):
        p1 = Point(220,70)
        p2 = Point(205,120)
        p3 = Point(230,125)
        p4 = Point(267,120)
        p5 = Point(300,140)
        p6 = Point(324,127)
        p7 = Point(236,210)
        p8 = Point(252,215)
        p9 = Point(230,239)
        p10 = Point(215,245)
        p11 = Point(200,280)
        p12 = Point(260,260)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)
        self.plot(p8)
        self.plot(p9)
        self.plot(p10)
        self.plot(p11)
        self.plot(p12)

        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p4)
        self.drawLine(p1, p4)
        self.drawLine(p4, p7)
        self.drawLine(p4, p5)
        self.drawLine(p5, p6)
        self.drawLine(p5, p8)
        self.drawLine(p8, p12)
        self.drawLine(p7, p9)
        self.drawLine(p9, p12)
        self.drawLine(p9, p10)
        self.drawLine(p10, p11)

    # Plot Venatici constellation 
    def plotVenatici(self):
        p1 = Point(170,350)
        p2 = Point(390,60)

        self.plot(p1)
        self.plot(p2)

        self.drawLine(p1, p2)
   
    # Plot Chamaeleon constellation 
    def plotChamaeleon(self):
        p1 = Point(550,230)
        p2 = Point(275,225)
        p3 = Point(75,260)
        p4 = Point(260,290)
        p5 = Point(530,242)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)

        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p4)
        self.drawLine(p4, p5)
        
    # Plot Draco constellation 
    def plotDraco(self):
        p1 = Point(195,255)
        p2 = Point(180,265)
        p3 = Point(155,250)
        p4 = Point(180,230)
        p5 = Point(190,95)
        p6 = Point(180,60)
        p7 = Point(245,85)
        p8 = Point(253,105)
        p9 = Point(237,175)
        p10 = Point(250,245)
        p11 = Point(245,260)
        p12 = Point(255,265)
        p13 = Point(330,275)
        p14 = Point(405,310)
        p15 = Point(420,320)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)
        self.plot(p8)
        self.plot(p9)
        self.plot(p10)
        self.plot(p11)
        self.plot(p12)
        self.plot(p13)
        self.plot(p14)
        self.plot(p15)

        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p4)
        self.drawLine(p4, p1)
        self.drawLine(p4, p5)
        self.drawLine(p5, p6)
        self.drawLine(p6, p7)
        self.drawLine(p7, p8)
        self.drawLine(p8, p9)
        self.drawLine(p9, p10)
        self.drawLine(p10, p11)
        self.drawLine(p11, p12)
        self.drawLine(p12, p13)
        self.drawLine(p13, p14)
        self.drawLine(p14, p15)

    # Plot Crater constellation
    def plotCrater(self):
        p1 = Point(200,50)
        p2 = Point(275,70)
        p3 = Point(320,190)
        p4 = Point(450,280)
        p5 = Point(390,400)
        p6 = Point(300,260)
        p7 = Point(150,300)
        p8 = Point(100,270)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)
        self.plot(p8)

        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p4)
        self.drawLine(p4, p5)
        self.drawLine(p5, p6)
        self.drawLine(p6, p3)
        self.drawLine(p6, p7)
        self.drawLine(p7, p8)
        
    # Plot Vulpecula constellation
    def plotVulpecula(self):
        p1 = Point(130,170)
        p2 = Point(250,230)
        p3 = Point(285,250)
        p4 = Point(300,265)
        p5 = Point(395,280)
        p6 = Point(410,310)
        p7 = Point(150,240)

        self.plot(p1)
        self.plot(p2)
        self.plot(p3)
        self.plot(p4)
        self.plot(p5)
        self.plot(p6)
        self.plot(p7)

        self.drawLine(p1, p2)
        self.drawLine(p2, p3)
        self.drawLine(p3, p4)
        self.drawLine(p4, p5)
        self.drawLine(p4, p7)
        self.drawLine(p5, p6)
        
# Program Frame       
class Game(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
    # Sets up player input, text response, and canvas
    def setupGUI(self):

        # Create box for player input at the bottom of the window
        # Bind to the enter key and put it in focus so the player
        # Won't have to click on it
        Game.playerInput = Entry(self.master, bg = "white")
        Game.playerInput.bind("<Return>", self.process)
        Game.playerInput.pack(side = BOTTOM, fill = X)
        Game.playerInput.focus()

        # Text response for player's input
        Game.result = Label(self.master, bg = "black", fg = "yellow", text = "Enter passphrase")
        Game.result.pack(side = BOTTOM, fill = X)

        # Constellation canvas
        Game.sky = Constellation(self.master)
        Game.sky.pack(fill = BOTH, expand = 1)
        
        
    # Processes player input
    def process(self, event):

        # Take player input and make it lowercase
        con = Game.playerInput.get()
        con = con.lower()

        # Plots the constellations with phrase collected by completeing the other puzzles
        # Or tells them to try again if none of the accepted phrases are entered
        if (con == "the bird"):
            Game.sky.plotPhoenix()
            Game.result.config(text = "user/password")

        elif (con == "the bull"):
            Game.sky.plotTaurus()
            Game.result.config(text = "user/password")

        elif (con == "big dog"):
            Game.sky.plotCanisMajor()
            Game.result.config(text = "user/password")

        elif (con == "hunting dogs"):
            Game.sky.plotCanesVenatici()
            Game.result.config(text = "user/password")

        elif (con == "camo lizard"):
            Game.sky.plotChameleon()
            Game.result.config(text = "user/password")

        elif (con == "the dragon"):
            Game.sky.plotDraco()
            Game.result.config(text = "user/password")

        elif (con == "the cup"):
            Game.sky.plotCrater()
            Game.result.config(text = "user/password")

        elif (con == "the fox"):
            Game.sky.plotVulpecula()
            Game.result.config(text = "user/password")

        else:
            Game.result.config(text = "Try again.")
    

# Main part of the program

# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520

# the default point radius is 0 pixels and yellow
POINT_RADIUS = 2
POINT_COLOR = "yellow"

# default line color is yellow
LINE_COLOR = "yellow"

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Constellations")

# create the Constellation Canvas
s = Game(window)
s.setupGUI()

# wait for the window to close
window.mainloop()
