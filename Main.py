import os

from FileIO import *
from FileContainer import Container
from TextProcessing import *
from nltk.corpus import stopwords
from string import punctuation
from copy import copy
from math import log


def main():

    # get filepaths

    filepaths = generate_file_list(".", True)

    # terminate program if no paths

    if len(filepaths) < 1:
        print("No files found")
        return

    # invalid files are reported in error report
    # valid files are processed further

    containers, invalid_files = list(), list()

    # record vocabulary

    vocabulary = list()
    global_word_counts = dict()

    for index, path in enumerate(filepaths, 1):

        file_contents = read_file(path)

        if file_contents is False:  # file cannot be read
            invalid_files.append((index, path))
        else:                       # file can be read
            c = Container()
            c.path = path
            c.index = index

            # get each token, remove punctuation and make it lower case

            c.raw = file_contents
            c.tokens = word_tokenize(c.raw)
            c.normalised = [token.lower() for token in c.tokens if token not in punctuation] # token.lower() not in stopwords.words("english") and
            [vocabulary.append(token) for token in c.normalised if token not in vocabulary]

            for word in c.normalised:

                if word not in global_word_counts:
                    global_word_counts[word] = 1
                else:
                    global_word_counts[word] = global_word_counts[word] + 1

            c.term_frequencies = dict()

            containers.append(c)

    # calculate term frequencies for each term in each file

    for container in containers:
        for word in vocabulary:
            container.term_frequencies[word] = container.normalised.count(word) / len(container.normalised)

    default_frequency_map = dict()

    for word in vocabulary:
        default_frequency_map[word] = 1

    # debugging test

    document = containers[0]

    print(document.term_frequencies["learning"] * calculate_idf("learning", [c.normalised for c in containers]))


"""
Takes two TD-IDF vectors
Returns dot product of vectors
"""


def dot_product(document1, document2):
    result = 0
    for i in range(0, len(document1)):
        result += document1[i] * document2[i]
    return result


if __name__ == "__main__":
    main()
