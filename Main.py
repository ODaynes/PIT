import os

from FileIO import *
from FileContainer import Container
from TextProcessing import *
from VectorMaths import *

from nltk.corpus import stopwords
from nltk.stem import snowball
from string import punctuation


def main():

    threshold = 0.5

    # get filepaths

    filepaths = generate_file_list("./data", True)

    # terminate program if no paths

    if len(filepaths) < 1:
        print("No files found")
        return

    # invalid files are reported in error report
    # valid files are processed further

    containers, invalid_files = list(), list()

    # record vocabulary

    vocabulary = list()
    #global_word_counts = dict()

    stemmer = snowball.EnglishStemmer()



    for index, path in enumerate(filepaths, 1):

        file_contents = read_file(path)

        if file_contents is False:  # file cannot be read
            invalid_files.append((path, "File is not in an acceptable format."))
            continue
        else:                       # file can be read
            print("Parsing %s" % path)
            c = Container()
            c.path = path
            c.index = index

            # get each token, remove punctuation and make it lower case

            c.raw = file_contents

            print("Retrieved raw text")

            c.tokens = word_tokenize(c.raw)

            print("Tokenised")

            c.normalised = [stemmer.stem(token.lower()) for token in c.tokens if token not in punctuation and token.lower() not in stopwords.words("english")] # token.lower() not in stopwords.words("english") and

            print("Normalised")

            [vocabulary.append(token) for token in c.normalised if token not in vocabulary]

            # for word in c.normalised:
            #
            #     if word not in global_word_counts:
            #         global_word_counts[word] = 1
            #     else:
            #         global_word_counts[word] = global_word_counts[word] + 1

            c.term_frequencies = dict()
            c.inverse_document_frequencies = dict()

            containers.append(c)

            print("File %s parsed" % path)

    # collect normalised documents in a single list to be used in idf calculation

    normalised_documents = [container.normalised for container in containers]

    print("Normalised documents gathered")

    # calculate term frequencies and inverse document frequencies for each term in each file

    print("Calculating inverse document frequencies")


    idf = dict()

    for word in vocabulary:
        idf[word] = calculate_idf(word, normalised_documents)

    print("Calculating term frequencies")

    for container in containers:
        for word in vocabulary:
            #if container.normalised.count(word) > 0:
            container.term_frequencies[word] = container.normalised.count(word) / len(container.normalised)
            # container.inverse_document_frequencies = idf.copy()
        # container.vector = create_document_vector(container)

    print("Copying idfs")

    for container in containers:
        container.inverse_document_frequencies = idf.copy()

    print("Calculated term frequencies and inverse document frequencies")

    # default_frequency_map = dict()

    # for word in vocabulary:
    #     default_frequency_map[word] = 1

    # calculate similarity between all valid files

    # vector_x, vector_y = create_dense_vectors(containers[0], containers[3])
    # print(vector_x)
    # print(vector_y)

    print("Now comparing documents")

    results = []

    for x in range(0, len(containers)):
        for y in range(x + 1, len(containers)):
            container_x = containers[x]
            container_y = containers[y]

            vector_x, vector_y = create_dense_vectors(container_x, container_y)

            if len(vector_x) == 0 or len(vector_y) == 0:
                similarity = 0.0
            else:
                similarity = cosine_similarity(vector_x, vector_y)

            #if similarity >= threshold:
            results.append((container_x.path, container_y.path, similarity))

    print(results)

    string = generate_html_string(results, invalid_files, threshold)
    write_string_to_file(string, "similarity_report.html")

    print("Report generated")

if __name__ == "__main__":
    main()
