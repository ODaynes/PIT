"""
FileIO.py should include all methods used to read
and write files.

Designed and created by Owen Daynes.

DOCX is a library designed to create and update Microsoft Word files.
More information can be found here: https://python-docx.readthedocs.io/en/latest/

docx2txt is a library designed to extract text from doc and docx files.
More information can be found here: https://github.com/ankushshah89/python-docx2txt

PyPDF2 is a library designed to read and write pdf files.
More information can be found here: https://github.com/mstamy2/PyPDF2
"""

import os

import docx2txt
import PyPDF2


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
    if ext == "pdf":
        return read_pdf(filepath)
    
    # file could not be read
    return False


"""
Returns a single string of all text within the txt file.
"""


def read_txt(filepath):
    result = ""

    with open(filepath, "r") as f:
        lines = f.readlines()

    for line in lines:
        for word in line.split():
            result += word + " "

    return result

"""
Returns a single string of all text within the doc or docx file.
"""


def read_docx(filepath):
    return docx2txt.process(filepath)

"""
Returns a single string of all text within the pdf file.
"""


def read_pdf(filepath):
    file_obj = open(filepath, "rb")
    reader = PyPDF2.PdfFileReader(file_obj)

    result = ""
    for i in range(0, reader.numPages):
        result += reader.getPage(i).extractText().replace("\n", "")
    return result

"""
Returns a list of all files within a directory.
Returns an empty list if invalid directory 
or a list of length one if a filepath is provided
Searches all sub-directories if recursive flag is true.
"""


def generate_file_list(directory, recursive=True):
    result = []
    print(directory)
    if os.path.isfile(directory):
        result.append(os.path.abspath(directory))

    if not os.path.isfile(directory):
        if os.path.isdir(directory):
            for path in os.listdir(directory):
                abs_path = os.path.abspath(path)
                print(abs_path)
                if os.path.isdir(abs_path) and recursive:
                    result += generate_file_list(abs_path, True)
                else:
                    result.append(abs_path)
    return result
