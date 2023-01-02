import os
import PyPDF2
import docx

def pdf_to_docx(pdf_path, docx_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF object
        pdf = PyPDF2.PdfFileReader(file)

        # Create a DOCX file
        docx = docx.Document()

        # Iterate through each page of the PDF
        for page in range(pdf.getNumPages()):
            # Extract the text from the page
            text = pdf.getPage(page).extractText()

            # Add the text to the DOCX document
            docx.add_paragraph(text)

        # Save the DOCX file
        docx.save(docx_path)

# Test the function
if __name__ == '__main__':
    pdf_path = 'engine.pdf'
    docx_path = 'engine.docx'
    pdf_to_docx(pdf_path, docx_path)
    print('Successfully converted PDF to DOCX!')
