import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk



import os
import comtypes.client

def pdf_to_docx(pdf_path, docx_path):
    # Open the PDF file in read binary mode
    with open(pdf_path, 'rb') as file:
        # Convert the PDF to a DOCX file
        comtypes.client.CreateObject('Word.Application').Documents.Open(file.name).SaveAs(docx_path, 16)

# Test the function
if __name__ == '__main__':
    pdf_path = 'path/to/input.pdf'
    docx_path = 'path/to/output.docx'
    pdf_to_docx(pdf_path, docx_path)
    print('Successfully converted PDF to DOCX!')
