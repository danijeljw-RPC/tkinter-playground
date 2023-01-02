# Importing the Converter() class
from pdf2docx import Converter

# Specifying the pdf & docx files
pdf_file = 'sample.pdf'
docx_file = 'sample.docx'


try:
    # Converting PDF to Docx
    cv_obj = Converter(pdf_file)
    cv_obj.convert(docx_file)
    cv_obj.close()

except:
    print('Conversion Failed')
    
else:
    print('File Converted Successfully')