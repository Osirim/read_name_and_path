"""This program opens and read a text file, strip off whitespaces,
 split the name into two variables - first and last name
  and print the results """
import os

file_path = r"C:\Users\Temu\Desktop\Bicome Assignemts\Bicom Assignment 2\read_name\name.txt"

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        full_name = file.read().strip()
        first_name, last_name = full_name.split()
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Full name:", full_name)
else:
    print('File path doesn\'t exist')