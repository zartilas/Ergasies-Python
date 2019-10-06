from FileManager import *

ascii_string = ascii_string = set("[\b][\t][U+2207][U+007f] ")

total_count = len(load_paragraph())
ascii_count = sum(c in ascii_string for c in load_paragraph())

print("Total number of characters:", total_count)
print("Total number of ASCII characters:", ascii_count)
print("Total number of non-ASCII characters:", total_count - ascii_count)

# import re
#
# replchars = re.compile(r'[\n\r]')
#
#
# def replchars_to_hex(match):
#     return r'\x{0:02x}'.format(ord(match.group()))
#
#
# print(replchars.sub(replchars_to_hex, load_paragraph()))
