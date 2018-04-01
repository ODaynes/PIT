import unittest
import FileIO


class TestFileIO(unittest.TestCase):

    def test_load_txt(self):
        contents = FileIO.read_file("example_files/ExampleTXT.txt")
        assert contents is not False

    def test_load_docx(self):
        contents = FileIO.read_file("example_files/ExampleDOCX.docx")
        assert contents is not False

    def test_load_pdf(self):
        contents = FileIO.read_file("example_files/ExamplePDF.pdf")
        assert contents is not False

    def test_load_other_format(self):
        contents = FileIO.read_file("TestFileIO.py")
        assert contents is False