"""
A Linked List (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure. You can think of it as an implementation of a regular Python List.

Using Object Oriented programming, build a simple Linked List that shares the same interface with Python Lists:

    l = LinkedList()

    l.append(2)
    l.count()  # Should return 1

    l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
    l += [3, 4]   # Should return None and append [3, 4] to the original list

    l.pop(0)       # Should remove and return the first element.

    # Important. This should be True:
    LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])

To ease your task, a LinkedList is constructed using different Nodes. Each node has a reference to other Node, what makes it a recursive class, it'll point to itself.

"""

class Node(object):

    def __init__(self, elem, idx=None, next=None):
        self.elem = elem
        self.idx = idx
        self.next = next
        
    def __eq__(self, other):
        return self.elem == other
            
class LinkedList(object):
    
    def __init__(self, starting_elems=None):
        self.amount = 0
        self.start = None
        self.end = -1
        self.current = None
        if starting_elems is not None:
            if not isinstance(starting_elems, list):
                starting_list = [starting_elems]
            else:
                starting_list = starting_elems
            for x in starting_list:
                self.append(x)
        
    def __add__(self, other):
        ''' no mutation in original list '''
        if isinstance(other, list):
            extra_list = other
        elif isinstance(other, int): 
            extra_list = [other]
        elif isinstance(other, LinkedList):
            extra_list = other.return_all()
        cur_list = self.return_all()
        new_list = cur_list + extra_list
        return LinkedList(new_list)
         
    def __iadd__(self, other):
        '''mutation in original list'''
        if isinstance(other, list):
            extra_list = other
        elif isinstance(other, int): 
            extra_list = list(other)
        elif isinstance(other, LinkedList):
                extra_list = other.return_all()

        cur_all = self.return_all()
        for x in extra_list:
            cur_all.append(x)
        print ("cur_all is", cur_all)
        return LinkedList(cur_all)

    def __iter__(self):
        self.current = self.start
        return self
        
    def __next__(self):
        current_it = self.current
        if self.amount == 0 or current_it is None:
            raise StopIteration          
        self.current = self.current.next
        return current_it.elem
            
    def __str__(self):
        joined_nodes = ", ".join([str(node) for node in self])
        return "[{}]".format(joined_nodes)

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return [node for node in self] == [node for node in other]

    def append(self, new_value):
        self.amount += 1
        idx = self.amount-1
        new_node = Node(new_value, idx)
        if self.start == self.end:
            self.start.next = new_node
        if self.start is None:
            self.start = new_node
            self.end = new_node
            self.current = self.start
        else:
            self.end.next = new_node
            self.end = new_node

    def return_all(self):
        if self.start is None:
            return []
        self.current = self.start
        a_list = [self.current.elem]
        while self.current.next is not None:
            a_list.append(self.current.next.elem)
            self.current = self.current.next
        return a_list
        
    def count(self):
        return self.amount
    
    def pop(self, pos=None):
        if self.start is None:
            raise IndexError
        if pos is None:
            pos = self.end.idx
        if self.start.idx > pos or pos > self.end.idx:
            raise IndexError
            
        chk_node = self.start
        if chk_node.next is None:
            cur_node = chk_node
        else:
            
            if chk_node.idx == pos:
                cur_node = chk_node
                second_node = cur_node.next
                self.start = second_node
            else:
                while pos != chk_node.next.idx:
                    chk_node = chk_node.next
                else:
                    prev_node = chk_node
                    cur_node = chk_node.next
                    next_node = cur_node.next
                
                prev_node.next = next_node
        return_val = cur_node.elem
        self.amount -= 1
        del cur_node
        return return_val
        
'''
l = LinkedList()

l.append(6)
l.append(5)
l.append(10)
#l.append(10)
#l.append(10)
print("count is ", l.count())

print ("should be all of them", l.return_all())

print (l.pop(0))
print ("should be all of them", l.return_all())

k = LinkedList()

k.append(1)
print (k.return_all())

print (k + [2,3])
print (k + 3)

m = LinkedList()
n = m + 1
print (m.return_all())
print (n)



my_list = LinkedList()
print (my_list.return_all())
my_list += LinkedList([1, 2])

print (my_list.return_all())

print ("new tests")
m_list = LinkedList()
new_list = m_list + LinkedList([1])
print ("new list", new_list)
print (new_list.return_all())
print ("new list duplicate", LinkedList([1]))
print (LinkedList([1]).return_all())
print (LinkedList())
print (m_list)
'''

first = LinkedList()
print (first)
first.append(1)
print (first)
first.append(3)
print (first)
first.append(4)
print (first)
first.append(4)


if __name__ == "__main__":
    import unittest
    class LinkedListTestCase(unittest.TestCase):
        ListImplementationClass = LinkedList
        
        def test_creation_and_equal(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            self.assertTrue(l1.start is not None)
            self.assertEqual(l1.start.elem, 1)

            self.assertTrue(l1.end is not None)
            self.assertEqual(l1.end.elem, 3)

            self.assertTrue(l1.start.next is not None)
            self.assertEqual(l1.start.next.elem, 2)

            self.assertTrue(l1.start.next.next is not None)
            self.assertEqual(l1.start.next.next.elem, 3)

        def test_append(self):
            my_list = self.ListImplementationClass()

            my_list.append(1)
            self.assertEqual(my_list.start.elem, 1)
            self.assertEqual(my_list.start.next, None)
            self.assertEqual(my_list, self.ListImplementationClass([1]))

            my_list.append(2)
            self.assertEqual(my_list.start.elem, 1)
            self.assertEqual(my_list.start.next, Node(2))
            self.assertEqual(my_list.start.next.elem, 2)
            self.assertEqual(my_list.start.next.next, None)

            self.assertEqual(my_list.count(), 2)

        def test_count(self):
            self.assertEqual(self.ListImplementationClass([1, 2, 3]).count(), 3)

        def test_pop_removes_last_item_by_default(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop()
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([1, 2]))

        def test_pop_removes_first_item(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop(0)
            self.assertEqual(elem, 1)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([2, 3]))

        def test_pop_removes_last_item(self):
            l1 = self.ListImplementationClass([1, 2, 3])

            elem = l1.pop(2)
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 2)
            self.assertEqual(l1, self.ListImplementationClass([1, 2]))

        def test_pop_removes_item_in_the_middle_of_the_list(self):
            l1 = self.ListImplementationClass([1, 2, 3, 4, 5])

            elem = l1.pop(2)
            self.assertEqual(elem, 3)
            self.assertEqual(l1.count(), 4)
            self.assertEqual(l1, self.ListImplementationClass([1, 2, 4, 5]))

            elem = l1.pop(1)
            self.assertEqual(elem, 2)
            self.assertEqual(l1.count(), 3)
            self.assertEqual(l1, self.ListImplementationClass([1, 4, 5]))

        def test_pop_with_a_single_element_list(self):
            # Default index
            l1 = self.ListImplementationClass([9])

            elem = l1.pop()
            self.assertEqual(elem, 9)
            self.assertEqual(l1.count(), 0)
            self.assertEqual(l1, self.ListImplementationClass([]))

            # index == 0
            l1 = self.ListImplementationClass([9])

            elem = l1.pop(0)
            self.assertEqual(elem, 9)
            self.assertEqual(l1.count(), 0)
            self.assertEqual(l1, self.ListImplementationClass([]))

        def test_pop_raises_an_exception_with_empty_list(self):
            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop()

            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop(0)

            with self.assertRaises(IndexError):
                self.ListImplementationClass().pop(3)

        def test_pop_raises_an_exception_with_invalid_index(self):
            with self.assertRaises(IndexError):
                self.ListImplementationClass([1]).pop(1)

            with self.assertRaises(IndexError):
                self.ListImplementationClass([1, 2, 3]).pop(3)

        def test_equals(self):
            self.assertEqual(
                self.ListImplementationClass([1, 2, 3]),
                self.ListImplementationClass([1, 2, 3]))

            self.assertEqual(
                self.ListImplementationClass([]),
                self.ListImplementationClass([]))

            self.assertEqual(
                self.ListImplementationClass([1]),
                self.ListImplementationClass([1]))

            self.assertNotEqual(
                self.ListImplementationClass([1, 2]),
                self.ListImplementationClass([1, 2, 3]))

            self.assertNotEqual(
                self.ListImplementationClass([1]),
                self.ListImplementationClass([]))

        def test_add_list(self):
            my_list = self.ListImplementationClass()
            new_list = my_list + self.ListImplementationClass([1])
            self.assertEqual(new_list, self.ListImplementationClass([1]))
            self.assertEqual(my_list, self.ListImplementationClass())

            my_list = self.ListImplementationClass([1, 2])
            new_list = my_list + self.ListImplementationClass([3, 4])
            self.assertEqual(new_list, self.ListImplementationClass([1, 2, 3, 4]))
            self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

            my_list = self.ListImplementationClass([1, 2])
            new_list = my_list + self.ListImplementationClass()
            self.assertEqual(new_list, self.ListImplementationClass([1, 2]))
            self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

            my_list = self.ListImplementationClass()
            new_list = my_list + self.ListImplementationClass()
            self.assertEqual(new_list, self.ListImplementationClass())
            self.assertEqual(new_list.count(), 0)
            self.assertEqual(my_list, self.ListImplementationClass())
            self.assertEqual(my_list.count(), 0)

        def test_str(self):
            my_list = self.ListImplementationClass([1, 2, 3])
            self.assertEqual(str(my_list), "[1, 2, 3]")

            my_list = self.ListImplementationClass()
            self.assertEqual(str(my_list), "[]")

            my_list = self.ListImplementationClass([])
            self.assertEqual(str(my_list), "[]")

        def test_add_equals_list(self):
            my_list = self.ListImplementationClass()
            my_list += self.ListImplementationClass([1, 2])
            self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

            my_list = self.ListImplementationClass([1, 2])
            my_list += self.ListImplementationClass([3, 4])
            self.assertEqual(my_list, self.ListImplementationClass([1, 2, 3, 4]))

            my_list = self.ListImplementationClass([1, 2])
            my_list += self.ListImplementationClass()
            self.assertEqual(my_list, self.ListImplementationClass([1, 2]))

            my_list = self.ListImplementationClass()
            my_list += self.ListImplementationClass()
            self.assertEqual(my_list.count(), 0)
            self.assertEqual(my_list, self.ListImplementationClass())
            
    unittest.main()
    
