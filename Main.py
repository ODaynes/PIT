import os

from FileIO import *
from FileContainer import Container
from TextProcessing import *
from nltk.corpus import stopwords
from string import punctuation
from copy import copy



def main():

    filepaths = generate_file_list(".", True)

    if len(filepaths) < 1:
        print("No files found")
        return

    containers = list()
    raw_contents, invalid_files = list(), list()
    vocabulary = list()
    global_word_counts = dict()
    word_counts = dict()
    raw_files = list()
    tokenised_files = list()

    for index, path in enumerate(filepaths, 1):
        file_contents = read_file(path)
        if file_contents is False:
            invalid_files.append((index, path))
        else:
            c = Container()
            c.path = path
            c.index = index
            c.raw = file_contents
            c.tokens = word_tokenize(file_contents)
            c.lowered_tokens_no_stopwords = [token.lower() for token in c.tokens if token.lower() not in stopwords.words("english") and token not in punctuation]
            [vocabulary.append(token) for token in c.lowered_tokens_no_stopwords if token not in vocabulary]
            for word in c.lowered_tokens_no_stopwords:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] = word_counts[word] + 1

                if word not in global_word_counts:
                    global_word_counts[word] = 1
                else:
                    global_word_counts[word] = global_word_counts[word] + 1

            c.term_counts = word_counts

            term_freqs = dict()

            for term, count in c.term_counts.items():
                freq = count/len(c.lowered_tokens_no_stopwords)
                term_freqs[term] = freq

            c.term_frequencies = term_freqs

            containers.append(c)
            # raw_contents.append((index, file_contents))

    print(word_counts)

    print(vocabulary)
    default_frequency_map = dict()
    frequencies = list()

    for word in vocabulary:
        default_frequency_map[word] = 1

    for container in containers:
        f = copy(default_frequency_map)
        for word in container.lowered_tokens_no_stopwords:
            f[word] = f[word] + 1
        frequencies.append(f)

    # print(frequencies[0])
    # print(frequencies[1])

    similarity = 0

    for key, value in frequencies[0].items():
        print(key)
        s = (value/len(frequencies[0])) * (frequencies[1][key]/len(frequencies[1]))
        print(s)
        similarity += s

    print(similarity)

    #
    # if len(raw_contents) > 1:
    #     for raw in raw_contents:
    #         print(remove_punctuation(raw[1]))
    #else:
    #    print("None of files entered could be read. Only txt, doc, docx and pdf files can be read using this program.")

    # for index, path in enumerate(filepaths, 1):
    #     file_text = read_file(path)
    #     if file_text is not False:
    #         raw_files.append(file_text)
    #
    #     if not file_text:
    #         invalid_files.append((index, path))
    #     else:
    #         c = Container(path, index, file_text)
    #         valid_files.append(c)
    #
    # if len(valid_files) < 1:
    #     print("None of files entered could be read. Only txt, doc, docx and pdf files can be read using this program.")
    # else:
    #     for file in raw_files:
    #         tokenised_files.append(word_tokenize(remove_punctuation(file)))
    #     print(raw_files)
    #     print(tokenised_files)
    #     #tokenised_files =
    #
    # return



if __name__ == "__main__":
    a = 1
    b = a
    b += 1
    print(a)
    main()
