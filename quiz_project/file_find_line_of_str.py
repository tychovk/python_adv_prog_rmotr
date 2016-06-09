"""
Write a function, that receives a file path and a string as parameters, and
returns the line number where that string is in the file. If the string
is not in the file, it should return None.

Example:
  which_line('file1.txt', 'hello world')  # 10
  which_line('file1.txt', 'this is not in the file')  # None

"""


def which_line(filepath, a_string):
    with open(filepath, 'r') as f:
        for index, line in enumerate(f.readlines()):
            if a_string in line:
                return index + 1
        return None