#! python3
"""
Project:    Sandbox
Filename:   openpyxl_test
Created by: PJC
Created on: June 23, 2016
"""

import logging
import PyPDF2

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

pdf_filename = 'PDF_Original.pdf'
text_file = 'PDF_Text.txt'

# Create PDF Read object
logger.info('Prepping the PDF file: {0}\n'.format(pdf_filename))
pdf_file = open(pdf_filename, 'rb')
pdf_reader_obj = PyPDF2.PdfFileReader(pdf_file)

# Display information about pdf_reader_obj
logger.info('Document Information:  \n  {0}'.format(pdf_reader_obj.documentInfo))
logger.info('PDF Encrypted:  {0}'.format(pdf_reader_obj.isEncrypted))
logger.info('Total pages:  {0}'.format(pdf_reader_obj.numPages))
logger.info('Page Layout:  {0}'.format(pdf_reader_obj.pageLayout))
logger.info('Page Mode:  {0}\n'.format(pdf_reader_obj.pageMode))

# Open dst_file to write text to
logger.info('Opening {0} for writing'.format(text_file))
with open(text_file, 'w', encoding='utf-8') as fh:

    # For each page in PDF file add the text to the TXT file
    for page in range(pdf_reader_obj.numPages):
        logger.info('Working on page {0}'.format(page + 1))
        page_object = pdf_reader_obj.getPage(page)
        page_text = page_object.extractText()

        logger.debug(page_text)

        fh.write(page_text)

logger.info('Closing {0}'.format(text_file))
