"""
Write a function, that receives the path to a text file and sorts all the
lines in the file ascending or descending, depending on the 'sorting'
parameter.

Example:
  sort_lines('file1.txt', sorting='asc')
  sort_lines('file1.txt', sorting='desc')


"""


def sort_lines(filepath, sorting='asc'):
    with open(filepath, 'r') as f:
        all_lines = f.readlines()

    if sorting == "desc":
        lines_sorted = (sorted(all_lines, reverse=True))
    else:
        lines_sorted = (sorted(all_lines))

    with open(filepath, 'w') as g:
        for line in lines_sorted:
            g.write(line)