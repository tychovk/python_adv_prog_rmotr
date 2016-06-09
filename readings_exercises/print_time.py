'''
http://www.greenteapress.com/thinkpython/html/thinkpython017.html
Exercise 1  
Write a function called print_time that takes a Time object and prints it in the form hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least two digits, including a leading zero if necessary.
Exercise 2  
Write a boolean function called is_after that takes two Time objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement.


'''

import datetime

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    pass
    

    
the_time = Time()
the_time.hour = 11
the_time.minute = 59
the_time.second = 30


def print_time(our_time):
    print ("{:02.0f}:{:02.0f}:{:02.0f}".format(our_time.hour, our_time.minute, our_time.second))
    
    

print_time(the_time) 

def is_after(t1, t2):
    if t1 > t2:
        return True
    return False
    
    
    
t1 = print_time(datetime.datetime.now())




def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
   
    return sum
    
start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 140

done = add_time(start, duration)
print_time(done)    
    
    
def increment(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.minute += (time.second - time.second % 60) / 60
        time.second = time.second % 60
        
    if time.minute >= 60:
        time.hour += (time.minute - time.minute % 60) / 60
        time.minute = time.minute % 60
    
    return time
    

done2 = increment(start, 60)
print_time(done2)
















print ('\n\n\n')


########################################################################

class Cookie:
    DEFAULT_COLOR = 'blue'
    
    def __init__(self, b1=None, b2=None):
        if b1 is None:
            b1 = Cookie.DEFAULT_COLOR
        if b2 is None:
            b2 = Cookie.DEFAULT_COLOR
            
        self.button1 = 'red' 
        self.button2 = 'red' 
        
        
c1 = Cookie()

class CookieFactory(object):
    def __init__(self, number_of_instances):
        self.number_of_instances = number_of_instances
        
    def build(self):
        cookies = []
        for i in range(self.number_of_instances):
            cookies.append(Cookie())
        return cookies

factory = CookieFactory(number_of_instances=5)
cookies = factory.build()
print (cookies[0].button1)

for cookie in cookies:
    print (cookie.button1)

    
    
    
###########################################################################

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print (list1)
print (list2)
print (list3)

class Cookie:
    DEFAULT_COLOR = 'blue'
    
    def __init__(self, b1=None, b2=None):
        if b1 is None:
            b1 = Cookie.DEFAULT_COLOR
        else:
            self.b1
        if b2 is None:
            b2 = Cookie.DEFAULT_COLOR
            
        self.button1 = b1
        self.button2 = b2
        
    @classmethod
    def build_some_instances(cls, number_of_instances):
        cookies = []
        for i in range(number_of_instances):
            cookies.append(cls())
        return cookies
        
        
        
cookies = Cookie.build_some_instances(number_of_instances = 5)        
print (" C1, button1: {}".format(cookies[0].button1)) 
        