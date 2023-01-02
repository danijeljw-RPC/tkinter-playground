import sys
if sys.version_info[0] == 3:
    from tkinter import *
else:
    from Tkinter import *
    
root = Tk()  # create parent window

def volumeUp():
    '''output message to terminal to tell that the button is working'''
    print("Volume Increase +1")

def volumeDown():
    '''output message to terminal to tell that the button is working'''
    print("Volume Decrease -1")

# use Button and Label widgets to create a simple TV remote
def turnOnTV():
    '''callback method used for turn_on button'''
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(root)
    window.title("TV")
    image = PhotoImage(file="8899da2f65fb5a3731ca6c7c29901f11.gif")

    original_image = Label(window, image=image)
    original_image.image = image
    original_image.pack()

turn_on = Button(root, text="ON", command=turnOnTV)
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=volumeUp)
vol_up.pack()

vol_down = Button(root, text="-", command=volumeDown)
vol_down.pack()

root.mainloop()