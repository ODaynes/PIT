"""
FileIO.py should include all methods used to read
and normalise files before both comparison.

Designed and created by Owen Daynes.

DOCX is a library designed to create and update Microsoft Word files.
More information can be found here: https://python-docx.readthedocs.io/en/latest/

docx2txt is a library designed to extract text from doc and docx files.
More information can be found here: https://github.com/ankushshah89/python-docx2txt
"""

import os

import docx
import docx2txt


def get_extension(filepath):
    return os.path.splitext(filepath)[1][1:].lower()


""" 
Generic method to get text from file
Calls read_txt, read_doc and read_docx
dependant on file extension.
"""


def read_file(filepath):

    ext = get_extension(filepath)

    if ext == "txt":
        return read_txt(filepath)
    if ext == "doc" or ext == "docx":
        return read_docx(filepath)

    return "Invalid file format"


"""
Returns a single string of all text within the file.
"""


def read_txt(filepath):
    result = ""

    with open(filepath, "r") as f:
        lines = f.readlines()

    for line in lines:
        for word in line.split():
            result += word + " "

    return result


def read_doc(filepath):
    return


def read_docx(filepath):
    return docx2txt.process(filepath)


def normalise(document):
    return


def normalise_doc(document):
    return


def normalise_docx(document):
    return


def normalise_txt(document):
    return
