"""
FileContainer.py should include all methods and class definitions
relating to the storage of file information.

Designed and created by Owen Daynes.
"""


import FileIO


class Container:

    def __index__(self):
        self.path = ""

    # def __init__(self, filepath):
    #     self.filepath = filepath
    #     self.raw = FileIO.read_file(filepath)
    #     self.processed = ""
    #
    # def __init__(self, filepath, id, plaintext):
    #     self.filepath = filepath
    #     self.id = id
    #     self.raw = plaintext
    #     self.tokenised = ""
    #     self.stems = ""
    #     self.frequencies = dict()

    def path(self):
        return self.filepath

    def raw(self):
        return self.raw

    def tokens(self):
        return self.tokenised

    def stems(self):
        return self.stems

    def frequencies(self):
        return self.frequencies

    def processed_contents(self):
        if self.processed == "":
            self.processed = FileIO.normalise(self.raw)
        return self.processed

