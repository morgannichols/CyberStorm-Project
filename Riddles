#####################################################################
###Constellation Riddles  for Cyber Storm Project
#####################################################################

from Tkinter import *

global team 
team = "Draco"

class Riddle(object):
	def __init__(self, team):
		self.team = team
		
	# getters and setters for the instance variables
	@property
	def team(self):
		return self._team
	
	@team.setter
	def team(self, value):
		self._team = value

class Game(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
	def setupGUI(self):
		#organize the GUI
		self.pack(fill=BOTH, expand=1)
		
		#setup the player input at the bottom of the GUI
		#the widget is a Tkinter Entry
		#set its background to white and bind the return key to the function process in the class
		#push it to the bottom of the GUI and let it fill horizontally
		#give it focus so the player doesn't have to click on it
		Game.player_input = Entry(self, bg="grey")
		Game.player_input.bind("<Return>", self.process)
		Game.player_input.pack(side=BOTTOM, fill=X)
		Game.player_input.focus()
		
		#setup the text to the right of the GUI
		#first, the frame in which the text will be placed
		text_frame = Frame(self, width=WIDTH / 2)
		#the widget is a Tkinter Text
		#disable it by default
		#don't let the widget control the frame's size
		Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
		Game.text.pack(fill=Y, expand=1)
		text_frame.pack(side=RIGHT, fill=Y)
		text_frame.pack_propagate(False)
		
		
	#sets the status displayed on the right of the GUI
	def setStatus(self, status):
		#enable the text widget, clear it, set it, and disable it
		Game.text.config(state=NORMAL)
		Game.text.delete("1.0", END)
		Game.text.insert(END, "Welcome to the Constellation Riddles Puzzle! Answer the riddle correctly to receive the password. " + status) 
	
		if (team == "Taurus"):
			Game.text.insert(END, "\n\nTwo stars for horns, and a cluster of seven help you find this creature hiding in the heavens. What is the constellation?" + status)
			Game.text.config(state=DISABLED)
			
		elif (team == "Canis Major"):
			Game.text.insert(END, "\n\nChasing a hare, Orion's large pup you will see. The brightest star in the sky, you meet in Harry Potter book 3. What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Phoenix"):
			Game.text.insert(END, "\n\nGalaxies and fiery wings, it can't be seen from where we are, but in December you might see its shooting stars. What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Canes Venatici"):
			Game.text.insert(END, "\n\nIt isn't named after the chicken, but it does include a pup.  It was supposed to be named after a club, but the translator had a mix-up.  What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Chamaeleon"):
			Game.text.insert(END, "\n\nPascal from Tangled, he doesn't change colors in the sky, but he is sticking out his tongue, in hopes of catching a fly. What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Draco"):
			Game.text.insert(END, "\n\nNever tickle a sleeping dragon, working for Hera was bliss. Try not to make him mad, or his father will hear about this. What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Crater"):
			Game.text.insert(END, "\n\nApollo got very angry, because the raven didn't think, so he threw them into the sky, the bird, the snake, and the drink. What is the constellation?")
			Game.text.config(state=DISABLED)
			
		elif (team == "Vulpecula"):
			Game.text.insert(END, "\n\nNear an eagle and a vulture, sits a fox having a snack. This is unfortuante for the goose, as survival skills he did lack. What is the constellation?")
			Game.text.config(state=DISABLED)
	
	def play(self):
		self.setupGUI()
		self.setStatus("")
		#self.createRiddles()

	#processes the player's input
	def process(self, event):
		#grab the player's input from the input at the bottom
		#of the GUI
		action = Game.player_input.get()
		#set the user's input to lowercase to make it easier to
		#compare the verb and noun to known values
		action = action.lower()
		#set a default response
		#split the user input into words separated by spaces
		#store the words in a list
		words = action.split()

		#the game only understands one or two word inputs
		if (len(words) == 1):
			
			if (team == "Taurus" and Game.player_input == "taurus"):
				response = "Correct!" 
			elif (team == "Phoenix" and words == "phoenix"):
				response = "Correct!"
			elif (team == "Chamaeleon" and words == "chamaeleon"):
				response = "Correct!"
			elif (team == "Draco" and Game.player_input == "draco"):
				response = "Correct!"
			elif (team == "Crater" and words == "crater"):
				response = "Correct!"
			elif (team == "Vulpecula" and words == "vulpecula"):
				response = "Correct!"
			else:
				response = "Incorrect."
		
		elif (len(words) == 2):
			if (team == "Canis Major" and words == "canis major"):
				response = "Correct!"
			elif (team == "Canes Venatici" and words == "canes venatici"):
				response = "Correct!"
			else:
				response = "Incorrect."
		#display the response on the right of the GUI
		#display the room'simage on the left of the GUI
		#clear the player's input
		self.setStatus(response)
		Game.player_input.delete(0, END)

#################################################################
#the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

#create the window
window = Tk()
window.title("Riddles")

#create the GUI as a Tkinter canvas inside the window
g = Game(window)
#play the game
g.play()

#wait for the window to close
window.mainloop()
