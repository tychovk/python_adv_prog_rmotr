"""
Write a function, that receives one or many file paths as parameters and returns
the name of the file with max amount of lines.

Example:
  max_lines('file1.txt', 'file2.txt')  # 'file1.txt
  max_lines('file1.txt')  # 'file1.txt
  max_lines('file1.txt', 'file2.txt', 'file3.txt)  # 'file3.txt

"""


def max_lines(*file_names):
    x = 0
    for file_name in file_names:
        with open(file_name, 'r') as f:
            if len(f.readline()) > x:
                max_lines_filename = file_name
    return max_lines_filename
