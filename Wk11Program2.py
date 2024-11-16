# 2:  Write a GUI program that
# displays your name and address when a "Show Info" button is clicked.
# There should also be a "Quit" button which exits the GUI.

import tkinter
import tkinter.messagebox

class MyGUI:
   #create method
    def name_address(self):
        # display an info dialog box
        tkinter.messagebox.showinfo("Name and Address","My name is Mackenzie Court. I live in Hendricks, MN.")  # (is 'showinfo' a function???)

    def __init__(self):
        # create main window widget
        self.main_window = tkinter.Tk()

    # -------------1st button-------------
        # create button widget.
        # text 'Name & Address" displayed on the Button.
        # info box displayed when user clicks button
        self.address_button = tkinter.Button(self.main_window, text="Name & Address", command=self.name_address) 

        # -------------2nd button-------------
        # create button widget.
        # The text 'Quit' is on the Button.
        # the button executes the quit method
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        # pack the Name & Address Button
        self.address_button.pack(ipadx=20, ipady=50)
        # pack the Quit Button
        self.quit_button.pack(ipadx=10, ipady=20)

# create main function
def main():
    # create a main window widget
    main_window = MyGUI()

    # enter the tkinter main loop
    tkinter.mainloop()

# call the main function (why do we write this???)
if __name__ == '__main__':
    main()				
