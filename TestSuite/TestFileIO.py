import unittest
import FileIO

from os import remove


class TestFileIO(unittest.TestCase):

    def test_read_txt(self):
        contents = FileIO.read_file("example_files/ExampleTXT.txt")
        assert contents is not False

    def test_read_docx(self):
        contents = FileIO.read_file("example_files/ExampleDOCX.docx")
        assert contents is not False

    def test_read_pdf(self):
        contents = FileIO.read_file("example_files/ExamplePDF.pdf")
        assert contents is not False

    def test_read_other_format(self):
        contents = FileIO.read_file("TestFileIO.py")
        assert contents is False

    def test_read_html(self):
        contents = FileIO.read_html("https://www.google.com")
        assert contents is not False

    def test_generate_file_list(self):
        NUMBER_OF_FILES = 4
        filelist = FileIO.generate_file_list("example_files", True)
        assert len(filelist) == NUMBER_OF_FILES

    def test_write_file(self):
        filename = "example.txt"
        example_text = "test input"

        FileIO.write_string_to_file(example_text, filename)
        result_text = FileIO.read_file(filename)
        remove(filename)

        assert example_text.strip() == result_text.strip()

    def test_generate_html_string(self):
        result_list = list()
        error_list = list()
        threshold = 0.7

        html_string = FileIO.generate_html_string(result_list, error_list, threshold)
        assert html_string is not ""