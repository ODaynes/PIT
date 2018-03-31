"""
FileContainer.py should include all methods and class definitions
relating to the storage of file information.

Designed and created by Owen Daynes.
"""


class Container:

    def __init__(self):
        self.path = ""
        self.index = -1
        self.raw = ""
        self.entities = list()
        self.tokens = list()
        self.normalised = list()
        self.term_frequencies = dict()
        self.idfs = dict()

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_raw_text(self, raw):
        self.raw = raw

    def get_raw_text(self):
        return self.raw

    def set_named_entities(self, entities):
        self.entities = entities

    def get_named_entities(self):
        return self.entities

    def set_token_list(self, tokens):
        self.tokens = tokens

    def get_token_list(self):
        return self.tokens

    def set_normalised_text_list(self, normalised):
        self.normalised = normalised

    def get_normalised_text_list(self):
        return self.normalised

    def set_term_frequencies(self, term_frequencies):
        self.term_frequencies = term_frequencies

    def get_term_frequencies(self):
        return self.term_frequencies

    def set_inverse_document_frequencies(self, idfs):
        self.idfs = idfs

    def get_inverse_document_frequencies(self):
        return self.idfs