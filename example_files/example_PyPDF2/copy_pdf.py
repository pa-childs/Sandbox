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

pdf_filename_one = 'PDF_Original.pdf'
pdf_filename_two = 'PDF_Copy.pdf'

# Create PDF Read and Write objects
logger.info('Setting Up For Copying')
pdf_file = open(pdf_filename_one, 'rb')
pdf_reader_obj = PyPDF2.PdfFileReader(pdf_file)
pdf_writer_obj = PyPDF2.PdfFileWriter()

# Display information about pdf_reader_obj
logger.info('Document Information:  \n  {0}'.format(pdf_reader_obj.documentInfo))
logger.info('PDF Encrypted:  {0}'.format(pdf_reader_obj.isEncrypted))
logger.info('Total pages:  {0}'.format(pdf_reader_obj.numPages))
logger.info('Page Layout:  {0}'.format(pdf_reader_obj.pageLayout))
logger.info('Page Mode:  {0}\n'.format(pdf_reader_obj.pageMode))

# For each page in PDF add the contents to the new PDF file
logger.info('Copying {0} Has Begun'.format(pdf_filename_two))
for page in range(pdf_reader_obj.numPages):
    logger.info('Adding Page {0}'.format(page + 1))
    pdf_writer_obj.addPage(pdf_reader_obj.getPage(page))

with open(pdf_filename_two, "wb") as fh:
    pdf_writer_obj.write(fh)

logger.info('Copying {0} Has Completed'.format(pdf_filename_two))
