#! python 3
"""
Created on June 23, 2016

@author: PJC
"""

import logging
import PyPDF2

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

pdf_filename_one = 'PDF_File.pdf'
pdf_filename_two = 'Watermark.pdf'
pdf_watermarked = 'PDF_Watermarked.pdf'

# Create PDF Read objects for the files
logger.info('Setting Up For Merging PDFs')
pdf_file_one = open(pdf_filename_one, 'rb')
pdf_document_obj = PyPDF2.PdfFileReader(pdf_file_one)
pdf_file_two = open(pdf_filename_two, 'rb')
pdf_watermark_obj = PyPDF2.PdfFileReader(pdf_file_two)

pdf_writer_obj = PyPDF2.PdfFileWriter()

# For each page in PDF add the contents to the new PDF file
new_pdf_page = pdf_watermark_obj.getPage(0)
new_pdf_page.mergePage(pdf_document_obj.getPage(0))

pdf_writer_obj.addPage(new_pdf_page)

with open(pdf_watermarked, "wb") as fh:
    pdf_writer_obj.write(fh)
