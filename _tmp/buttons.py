import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


def loadPdfButton(main_window):
    photo_load_pdf = tk.PhotoImage(file="istockphoto-1298834280-612x612.jpg")
    photo = photo_load_pdf.subsample(10,10)
    btn_load_pdf = tk.Button(main_window, image=photo)
    btn_load_pdf.pack()
