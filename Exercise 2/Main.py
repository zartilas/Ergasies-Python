from FileManager import *

file_exists('Plithos.txt')

# Non printable characters are (ascii table): 0-31 & 127, therefore 32 + 1 = 33 non printable characters
file = open('Plithos.txt', 'w+')
file.write("Number of all non printable characters: " + str(33) + "\n"
           + "\n"
           + "ASCII table of non-printable characters:\n"
           + "Dec  Char\n"
           + "---------\n")
non_ascii = ["\b", "\t", " ", "\u007F"]
for i in range(0, 4):
    file.write(str(ord(non_ascii[i])) + "  " + non_ascii[i]
               .replace(" ", "SPACE")
               .replace("\u007F", "DELETE")
               .replace("\b", "BACKSPACE")
               .replace("\t", "TAB")
               + "\n")
file.close()

