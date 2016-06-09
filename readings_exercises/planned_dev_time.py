# planned development time functions.
# http://www.greenteapress.com/thinkpython/html/thinkpython017.html

class Time:
    pass


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
    
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def print_time(time):
    print ("{:02.0f}:{:02.0f}:{:02.0f}".format(time.hour, time.minute, time.second))

    
def add_time(t1, t2):
    d = time_to_int(t1) + time_to_int(t2)
    return int_to_time(d)
    
def increment(time, seconds):
    d = time_to_int(time) + seconds
    return int_to_time(d)
    
start = Time()
start.hour = 2
start.minute = 43
start.second = 122

print_time(start)

start_int = time_to_int(start)
start_time = int_to_time(start_int)

print_time(start_time)

