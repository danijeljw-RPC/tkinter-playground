import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("300x300+50+50")

# create label in the window
text = tk.Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = tk.Label(root, text="-Maya Angelou")
text2.pack()

# create photo label in the window
image = tk.PhotoImage(file="gui/025.gif")
img = tk.Label(root, image=image)
img.pack()
root.mainloop()

# run app
root.mainloop()