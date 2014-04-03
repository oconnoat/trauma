#!/usr/bin/python

# -*- coding: utf-8 -*-

""" extract pages from the document """

import os
import sys

from PyPDF2 import PdfFileReader

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"

def extract_papers(pdf_file, paper_pages):
    """Take the PDF object and the page delimiters and split them"""
    for paper in paper_pages:
        with open( os.path.join('extracted_text', paper+'.txt'), 'w') as text_file:
            #explode the tuple range
            for page in range(*paper_pages[paper]):
                text_file.write(pdf_file.getPage(page).extractText().encode('utf-8'))

if __name__ == '__main__':
    data_filename = os.path.join('data','TraumaPapers_2009.pdf')

    #tuples representing the page ranges foe each paper
    #currently these run to the title to the end, but it might want to remove biblios
    paper_pages = { 'front': (0,1),
                    'paper1' : (1, 28),
                    'paper2' : (28, 65),
                    'paper3' : (65,104) }

    with open(data_filename, 'rb') as data_file:
        data_pdf = PdfFileReader(data_file)

        extract_papers(data_pdf, paper_pages)

