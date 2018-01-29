import FileIO
import FileContainer

# print(FileIO.read_file("C:\\Users\\admin\\PycharmProjects\\testPIT\\TestFiles\\TestTXT.txt"))
# print(FileIO.read_file("C:\\Users\\admin\\PycharmProjects\\testPIT\\TestFiles\\TestDoc.docx"))
print(FileIO.read_file("C:\\Users\\admin\\PycharmProjects\\testPIT\\TestFiles\\CE301 SRS.pdf"))

# print(FileIO.read_file("notafile"))

test = FileContainer.Container("C:\\Users\\admin\\PycharmProjects\\testPIT\\TestFiles\\TestTXT.txt")
print(test.path())
print(test.unmodified_contents())
