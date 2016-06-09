




def table_printer(table):
    max_elems = [len(list1) for list1 in table]
    max_len_ele = [max([len(word) for word in list1]) for list1 in table]
    lines = ''
    
    for x in range(max(max_elems)):
        for index, col in enumerate(max_len_ele):
            lines = lines + table[index][x].rjust(col+3)
            if x + 1 > index:
                continue
        print (lines)
        lines = ''

    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
             
print (table_printer(tableData))

