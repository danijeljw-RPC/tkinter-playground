import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

def volumeDown():
    '''output message to terminal to tell that hte button is working'''
    print("Volume Decrease -1")

# use Button and Label widgets to create a simple TV remote
def turnOnTV():
    '''callback method used for turn_on button'''
    tv_root = tk.Tk()
    
    # use a Toplevel widget to display an image in a new window
    window = tk.Toplevel()
    window.title("TV")
    image = tk.PhotoImage(file="8899da2f65fb5a3731ca6c7c29901f11.gif")
    original_image = tk.Label(window, image=image)
    original_image.image = image
    original_image.pack()
    tv_root.mainloop()