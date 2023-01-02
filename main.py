# Importing the Converter() class
from pdf2docx import Converter

# Specifying the pdf & docx files
pdf_file = 'orange.pdf'
docx_file = 'muscles.docx'


try:
    # Converting PDF to Docx
    cv_obj = Converter(pdf_file)
    cv_obj.convert(docx_file)
    cv_obj.close()

except:
    print('Conversion Failed')
    
else:
    print('File Converted Successfully')