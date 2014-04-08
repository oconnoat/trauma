#!/usr/bin/python

# -*- coding: utf-8 -*-

""" split pages from the document """
from __future__ import unicode_literals

import os
import sys
import codecs

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"

def split_papers(pdf_file, paper_pages):
    """Take the PDF filepath and the page delimiters and split them"""
    pdf_reader = PdfFileReader(file(pdf_file,'rb'))

    for paper in paper_pages:
        pdf_writer = PdfFileWriter()
        print paper
            #explode the tuple range
        for page in range(*paper_pages[paper]):
            pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.write(file(os.path.join('extracted_text',paper+'.pdf'),'wb'))

if __name__ == '__main__':
    data_filename = os.path.join('data','TraumaPapers_2009.pdf')

    #tuples representing the page ranges foe each paper
    #currently these run to the title to the end, but it might want to remove biblios
    paper_pages = { 'front': (0,1),
                   'paper1' : (1, 27),
                   'paper2' : (27, 64),
                   'paper3' : (64, 103),
                   'paper4' : (103, 129),
                   'paper5' : (129, 159),
                   'paper6' : (159, 182),
                   'paper7' : (182, 206),
                   'paper8' : (206, 225),
                   'paper9' : (225, 260),
                   'paper10' : (287, 307) }

    split_papers(data_filename, paper_pages)

