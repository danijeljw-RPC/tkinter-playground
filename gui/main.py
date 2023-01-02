import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

root = tk.Tk()
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")
root.mainloop()