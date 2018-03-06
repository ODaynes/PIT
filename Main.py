import os

from FileIO import *
from FileContainer import Container
from TextProcessing import *
from VectorMaths import *

from nltk.corpus import stopwords
from string import punctuation


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
            c.normalised = [token.lower() for token in c.tokens if token not in punctuation and token.lower() not in stopwords.words("english")] # token.lower() not in stopwords.words("english") and
            [vocabulary.append(token) for token in c.normalised if token not in vocabulary]

            for word in c.normalised:

                if word not in global_word_counts:
                    global_word_counts[word] = 1
                else:
                    global_word_counts[word] = global_word_counts[word] + 1

            c.term_frequencies = dict()
            c.inverse_document_frequencies = dict()

            containers.append(c)

    # collect normalised documents in a single list to be used in idf calculation

    normalised_documents = [container.normalised for container in containers]

    # calculate term frequencies and inverse document frequencies for each term in each file

    for container in containers:
        for word in vocabulary:
            if container.normalised.count(word) > 0:
                container.term_frequencies[word] = container.normalised.count(word) / len(container.normalised)
            container.inverse_document_frequencies[word] = calculate_idf(word, normalised_documents)
        container.vector = create_document_vector(container)


    default_frequency_map = dict()

    for word in vocabulary:
        default_frequency_map[word] = 1

    # calculate similarity between all valid files

    for x in range(0, len(containers)):
        for y in range(x + 1, len(containers)):
            container_x = containers[x]
            container_y = containers[y]

            vector_x, vector_y = create_dense_vectors(container_x, container_y)

            if len(vector_x) == 0 or len(vector_y) == 0:
                similarity = 0.0
            else:
                similarity = cosine_similarity(vector_x, vector_y)

            print(container_x.path, container_y.path, similarity)

def create_dense_vectors(container_x, container_y):
    shared_vocabulary = list(set(container_x.normalised).intersection(set(container_y.normalised)))
    # shared_vocabulary = set([term for term, frequency in container_x.term_frequencies.items() if frequency > 0]).intersection(set([term for term, frequency in container_y.term_frequencies.items() if frequency > 0]))
    new_x, new_y = list(), list()

    for term in shared_vocabulary:
        new_x.append(container_x.term_frequencies[term] * container_x.inverse_document_frequencies[term])
        new_y.append(container_y.term_frequencies[term] * container_y.inverse_document_frequencies[term])

    return new_x, new_y

#def new_cosine_similarity(vector_x, vector_y, )
if __name__ == "__main__":
    main()
