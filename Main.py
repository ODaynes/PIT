import os

import FileIO
from FileContainer import Container
import TextProcessing


def main():

    filepaths = FileIO.generate_file_list(".", True)

    if len(filepaths) < 1:
        print("No files found")
        return

    valid_files, invalid_files = list(), list()

    for index, path in enumerate(filepaths, 1):
        file_text = FileIO.read_file(path)
        if not file_text:
            invalid_files.append((index, path))
        else:
            c = Container(path, index, file_text)
            valid_files.append(c)

    if len(valid_files) < 1:
        print("None of files entered could be read. Only txt, doc, docx and pdf files can be read using this program.")
    else:
        for file in valid_files:
            print(file.unmodified_contents())
    return


if __name__ == "__main__":
    main()
