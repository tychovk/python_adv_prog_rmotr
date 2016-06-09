#try some stuff!
from random import randint


class RandomNumberIterator(object):
    def __init__(self, smallest=0, largest=1000):
        self.served = set()
        self.smallest = smallest
        self.largest = largest

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.served) == (self.largest - self.smallest + 1):
            raise StopIteration()

        while True:
            number = randint(self.smallest, self.largest)
            if number not in self.served:
                self.served.add(number)
                return number

    next = __next__
    
    
    
rand_num = RandomNumberIterator(1, 3)
for x in rand_num:
    print (x)

    
testtup = (1,3,4)

print (sum(testtup))

print (testtup[0] - sum(testtup[1:]))