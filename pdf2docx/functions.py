import sys
import os
if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import filedialog as fd
else:
    import Tkinter as tk
    from Tkinter import filedialog as fd
from pdf2docx import Converter


def convert_document(pdf_file,docx_file):
    global pd1
    global pd2

    pd1 = pdf_file
    pd2 = docx_file

    try:
        cv_obj = Converter(pd1)
        cv_obj.convert(pd2)
        cv_obj.close()
    except:
        print('Conversion Failed')
        tk.messagebox.showerror("Fail!!", "Something Went Wrong...")
    else:
        tk.messagebox.showinfo("success ", "your Image converted to GIF Format")

def pdf_to_docx():
    import_filename = fd.askopenfilename()
    if import_filename.endswith(".pdf"):
        export_filename = fd.asksaveasfilename(defaultextension=".docx")
        convert_document(pdf_file=import_filename,docx_file=export_filename)
    else:
        tk.messagebox.showerror("Fail!!", "Something Went Wrong...")

