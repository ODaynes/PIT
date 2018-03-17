import sys

from nltk.corpus import stopwords
from nltk.stem import snowball

from FileIO import *
from FileContainer import Container
from TextProcessing import *
from VectorMaths import *


def main(directory, threshold=0.7):

    try:
        threshold = float(threshold)
    except ValueError:
        print("Invalid threshold value provided.")
        print("Using default 0.7")
        threshold = 0.7

    if threshold > 1:
        threshold /= 100

    # get filepaths

    filepaths = generate_file_list(directory, True)

    # terminate program if no paths

    if len(filepaths) < 1:
        print("No files found")
        return

    # invalid files are reported in error report
    # valid files are processed further

    containers, invalid_files = list(), list()

    # record vocabulary

    vocabulary = list()

    stemmer = snowball.EnglishStemmer()

    for index, path in enumerate(filepaths, 1):

        try:
            file_contents = read_file(path)     # file can be opened
        except Exception:                       # file cannot be opened
            print("File %s could not be opened" % path)
            invalid_files.append((path, "File could not be opened."))
            continue

        if file_contents is False:  # file contents cannot be read
            invalid_files.append((path, "File is not in an acceptable format."))
            continue
        else:                       # file contents can be read
            print("Parsing %s" % path)
            c = Container()
            c.path = path
            c.index = index

            # store raw file contents

            c.raw = file_contents

            print("Retrieved raw text")

            # tokenise file conents

            c.tokens = word_tokenize(c.raw)

            print("Tokenised")

            # only keep token stems if tokens aren't punctuation or stop words

            c.normalised = [stemmer.stem(token.lower()) for token in c.tokens
                            if token not in punctuation and token.lower() not in stopwords.words("english")]

            print("Normalised")

            # cannot compare files with no text, report error and skip

            if len(c.normalised) < 1:
                print("File %s is either empty or contains no significant terms." % path)
                invalid_files.append((path, "File is either empty or contains no significant terms"))
                continue

            # add any new words to global vocabulary

            [vocabulary.append(token) for token in c.normalised if token not in vocabulary]

            # initialise frequency dictionaries

            c.term_frequencies = dict()
            c.inverse_document_frequencies = dict()

            # store container to allow further processing later

            containers.append(c)

            print("File %s parsed" % path)

    # collect normalised documents in a single list to be used in idf calculation

    normalised_documents = [container.normalised for container in containers]

    print("Normalised documents gathered")

    # calculate term frequencies and inverse document frequencies for each term in each file

    print("Calculating inverse document frequencies")

    inverse_document_frequencies = dict()

    for word in vocabulary:
        inverse_document_frequencies[word] = calculate_idf(word, normalised_documents)

    print("Calculating term frequencies")

    for container in containers:
        for word in vocabulary:
            container.term_frequencies[word] = container.normalised.count(word) / len(container.normalised)

    # shallow-copying already existing idf dict is faster than recreating each time

    for container in containers:
        container.inverse_document_frequencies = inverse_document_frequencies.copy()

    print("Calculated term frequencies and inverse document frequencies")

    print("Now comparing documents")

    results = []

    # calculate similarity for every pair of documents

    for x in range(0, len(containers)):
        for y in range(x + 1, len(containers)):
            container_x = containers[x]
            container_y = containers[y]

            vector_x, vector_y = create_dense_vectors(container_x, container_y)

            if len(vector_x) == 0 or len(vector_y) == 0:
                similarity = 0.0
            else:
                similarity = round(cosine_similarity(vector_x, vector_y), 4)

            if similarity >= threshold:
                results.append((container_x.path, container_y.path, similarity))

    # generate html string to write to file

    string = generate_html_string(results, invalid_files, threshold)

    # write html string to file

    write_string_to_file(string, "similarity_report.html")

    print("Report generated")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            main(sys.argv[1], sys.argv[2])
        else:
            main(sys.argv[1])
    else:
        main("./data")
