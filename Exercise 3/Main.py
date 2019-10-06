from FileManager import *
import re

pattern = re.compile('(?:/\*(.*?)\*/)|(?://(.*?)\n)',re.S)
comments = pattern.findall(load_paragraph())

print(*comments, sep='\n')
