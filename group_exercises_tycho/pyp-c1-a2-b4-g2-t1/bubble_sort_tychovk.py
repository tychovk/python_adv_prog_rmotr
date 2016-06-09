"""Bubble sort algorithm - Tycho van Kleef"""

test_list = [455,7,5,3,55,78,5,3,77,43,84,8986,32,345]
print (len(test_list))
def bubble_sort(uns_list):
    work_copy = uns_list[:]
    while True:
        c = 0
        adjust = 0
        while c + 1 < len(uns_list):
            if work_copy[c] > work_copy[c + 1]:
                work_copy[c], work_copy[c + 1] = work_copy[c + 1], work_copy[c]
                c += 1
                adjust = 1
            else:
                c += 1
                continue
        if adjust == 0:
            return work_copy
    

def insertion_sort(uns_list):
    work_copy = uns_list[:]
    for idx1, val1 in enumerate(work_copy):
        for idx2 in range(idx1, -1, -1):
            if idx2 == idx1:
                continue
            if idx2 == 0 and val1 < uns_list[idx2]:
                uns_list.insert(idx2, val1)
                del(uns_list[idx1 + 1])
                break    
            if val1 < uns_list[idx2]:
                continue
            else:
                uns_list.insert(idx2 + 1, val1)
                del(uns_list[idx1 + 1])
                break

    return uns_list


 
print ("The test list:")
print (test_list)
print ("The bubble sort:")
print (bubble_sort(test_list))

        
print ("The insertion sort:")
print (insertion_sort(test_list))



print (len([3, 3, 5, 5, 7, 32, 43, 55, 77, 78, 84, 345, 455, 8986]))
print (len([3, 3, 5, 5, 43, 32, 7, 55, 78, 77, 84, 8986, 345, 345]))