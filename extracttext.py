#!/usr/bin/python

# -*- coding: utf-8 -*-

""" extract pages from the document """
from __future__ import unicode_literals

import os
import sys

from glob import glob

from pdfminer.pdfparser import PDFParser, PDFDocument, PDFNoOutlines
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage


__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"


def extract_text(dir_path):
    """take the path and use PDFminer to write the text to a textfile of the same name"""
    dir_glob = glob(os.path.join(dir_path, '*.pdf'))
    for pdf_file in dir_glob:
        parser = PDFParser(open(pdf_file, 'rb'))
        document = PDFDocument()
        #set up the parser <--> document link
        parser.set_document(document)
        document.set_parser(parser)
        document.initialize()

        res_mgr = PDFResourceManager()
        device = PDFPageAggregator(res_mgr, laparams=LAParams())
        interpreter = PDFPageInterpreter(res_mgr, device)

        for page in doc.get_pages():
            interpreter.proxess_page(page)
            layout = device.get_result()
            #get only the text objects
            filter(lambda obj: isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine), layout)
            for text in layout:
                print text.get_text()

if __name__ == "__main__":
    dir_path='extracted_text'
    extract_text(dir_path)
