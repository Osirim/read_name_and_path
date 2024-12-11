"""This program reads the absolute file path of the name.txt file"""

import os

file_path = os.path.abspath("name.txt")
print("File path:", file_path)