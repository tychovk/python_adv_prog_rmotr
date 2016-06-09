"""
Write a function, that receives a path to two text files as parameters and copies
the content of the first file into the second, overwriting the content of the second
file if it's not empty.

Example:
  copy_file('test-file.txt', 'copy.txt')

"""

import os

def copy_file(source_file, target_file):
    if os.path.isfile(target_file) and os.path.getsize(target_file) != 0:
        return "file is not empty!"
    else:
        with open(source_file, 'r') as f:
            with open(target_file, 'w') as t:
                content = f.read()
                t.write(content)

