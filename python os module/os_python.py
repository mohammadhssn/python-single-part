"""
 os
    link: https://docs.python.org/3/library/os.html
"""

import os

print(os.getcwd())  # current directory
print(os.listdir())  # list directory

file = os.listdir()[0]

print(os.access(file, os.F_OK))  # found
print(os.access(file, os.R_OK))  # read
print(os.access(file, os.W_OK))  # write
print(os.access(file, os.X_OK))  # execute

print(os.environ)  # environments

# os.mkdir('first')  # create directory
os.rmdir('first')  # remove directory

os.makedirs('first/second')  # create nested directory
os.removedirs('first/second')  # remove nested directory
