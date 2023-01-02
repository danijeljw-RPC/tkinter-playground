import sys
if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import filedialog as fd
else:
    import Tkinter as tk
    from Tkinter import filedialog as fd
from pdf2docx import Converter
from PIL import Image

from functions import pdf_to_docx as p2d

# create main window
root = tk.Tk()
root.title("PDF 2 Word Doc Converter")
root.minsize(600, 500)

button1 = tk.Button(root,
            text="JPG_to_GIF",
            width=20,
            height=2,
            bg="green",
            fg="white",
            font=("helvetica", 12, "bold"),
            command=p2d())

button1.place(x=120, y=120)

root.geometry("500x500+400+200")
root.mainloop()
