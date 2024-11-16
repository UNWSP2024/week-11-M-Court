#import
import tkinter

class MyGUI:
		def __init__(self):	
				#create the main window widget
				self.main_window = tkinter.Tk()
				
				#create two Label widgets with solid borders
				self.label1 = tkinter.Label(self.main_window, text = "'The Gospels contain a faery-story, or a story of a larger kind which embraces all the essence of faery-stories.' --J.R.R. Tolkien")
				
				#display vertical and horizontal padding.
				self.label1.pack(ipadx = 20, ipady = 10)
				
				#enter the tkinter main loop.
				tkinter.mainloop()
				
#create an instance of the MyGUI class.
#if__name__ == "__main__":
my_gui = MyGUI()