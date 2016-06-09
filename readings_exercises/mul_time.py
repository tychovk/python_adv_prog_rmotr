# exercise 6 and 7
# http://www.greenteapress.com/thinkpython/html/thinkpython017.html

"""
Exercise 6  
Write a function called mul_time that takes a Time object and a number and 
returns a new Time object that contains the product of the original Time and the number.
Then use mul_time to write a function that takes a Time object that represents 
the finishing time in a race, and a number that represents the distance, and 
returns a Time object that represents the average pace (time per mile).
"""

class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    pass

def time_to_int(time):
    minute = time.hour * 60 + time.minute
    seconds = minute * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

    
def av_d_km_h(finishing_time, d_in_km):
    seconds = time_to_int(finishing_time)
    av_speed = seconds / d_in_km 
    av_time = int_to_time(av_speed)
    return av_time
    
def print_time(for_time):
    print ("{:02.0f}:{:02.0f}:{:02.0f}".format(for_time.hour, for_time.minute, for_time.second))
    
f_time = Time()
f_time.hour = 2
distance = 300

av_speed = av_d_km_h(f_time, distance)

print_time(f_time)
print_time(av_speed)


def hurr(haa = "2"):
    ask = input("durr?")
    return ask
    
print (hurr())