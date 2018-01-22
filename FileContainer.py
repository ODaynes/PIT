"""
FileContainer.py should include all methods and class definitions
relating to the storage of file information.

Designed and created by Owen Daynes.
"""


import FileIO


class Container:

    def __init__(self, filepath):
        self.filepath = filepath
        self.plain = FileIO.read_file(filepath)
        self.processed = ""

    def path(self):
        return self.filepath

    def unmodified_contents(self):
        return self.plain

    def processed_contents(self):
        if self.processed == "":
            self.processed = FileIO.normalise(self.plain)
        return self.processed

