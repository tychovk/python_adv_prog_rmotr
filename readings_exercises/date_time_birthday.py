"""
Exercise 7  
The datetime module provides date and time objects that are similar to the Date 
and Time objects in this chapter, but they provide a rich set of methods and 
operators. Read the documentation at http://docs.python.org/2/library/datetime.html.
Use the datetime module to write a program that gets the current date and 
prints the day of the week.

Write a program that takes a birthday as input and prints the user’s age and the 
number of days, hours, minutes and seconds until their next birthday.
For two people born on different days, there is a day when one is twice as old 
as the other. That’s their Double Day. Write a program that takes two birthdays 
and computes their Double Day.
For a little more challenge, write the more general version that computes the 
day when one person is n times older than the other.

"""

import datetime
import math

class Time():
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
def print_time(the_time):
    print ("{:02.0f}:{:02.0f}:{:02.0f}".format(the_time.hour, the_time.minute, the_time.second))
    
def time_to_int(time):
    minutes = time.hours * 60 + time.minutes
    seconds = minutes * 60
    
    return seconds
    
    
def int_to_time(seconds):
    time2 = Time()
    minute, time2.second = divmod(seconds, 60)
    time2.hour, time2.minute = divmod(minute, 60)
    
    return time2
    
def time_diff(t1, t2):
    s1 = time_to_int(t1)
    s2 = time_to_int(t2)
    d = s2 - s1
    d_time = int_to_time(d)
    
    return d_time
    
def check_legality(req_type = None, legal_range = None):
    def real_decorator(original_function):
        def new_function(*args, **kwargs):
            data = original_function(*args, **kwargs)
            if req_type == 'int':
                try:
                    number = int(data)
                    if legal_range is not None:
                        if number not in legal_range:
                            return new_function(*args, **kwargs)
                        else:
                            return number
                    else:
                        return number
                except Exception as e: 
                    return new_function(*args, **kwargs)
            else:
                if data in legal_range:
                    return data
                else:
                    return new_function(*args, **kwargs)
        return new_function
    return real_decorator
    
@check_legality(req_type = 'int', legal_range = range(1,32))
def ask_day():
    ask = input("On which day of the month were you born?")
    return ask
        
@check_legality(req_type = 'int', legal_range = range(1,13))
def ask_month():
    ask = input("In which month were you born?")
    return ask
    
@check_legality(req_type = 'int', legal_range = range(1900,datetime.datetime.now().year))
def ask_year():
    ask = input("And in which year?")
    return ask
        
def ask_birthday():
    day = ask_day()
    month = ask_month()
    year = ask_year()
    date_birth = datetime.datetime(year, month, day)
    return date_birth
    

def current_age(date_birth):
    current_date = datetime.datetime.now()
    age_datetime = diff_years(date_birth, current_date, check_d2_greater_d1 = True)

    return age_datetime

    
def time_to_next_bday(date_birth):
    now = datetime.datetime.now()
    if date_birth.month < now.month:
        next_bday_year = now.year + 1
    elif date_birth.month > now.month:
        next_bday_year = now.year
    elif date_birth.day > now.day:
        next_bday_year = now.year + 1
    elif date_birth.day < now.day:
        next_bday_year = now.year
    else:
        return "your birthday is today..."
    next_bday = datetime.datetime(next_bday_year, date_birth.month, date_birth.day)
    
    diff_seconds = diff_years(next_bday, now) * 60 * 60 * 24 * 365
    diff_date = datetime.datetime.fromtimestamp(diff_seconds)
    return diff_date
    

def diff_years(d1, d2, check_d2_greater_d1 = False):
    d1_sec = d1.timestamp()
    d2_sec = d2.timestamp()

    if check_d2_greater_d1 != False and d2_sec < d1_sec:
        print ("This will result in a negative time.. a negative age, e.g.")
        return False
    else:
        diff = math.sqrt((d2_sec - d1_sec) ** 2)
        d = diff / 60 / 60 / 24 / 365
        return d

def print_days(date):
    print ("{} days, {} months, {} years".format(date.day, date.month, date.year))
    
birthday = ask_birthday()
print (current_age(birthday))
diff_to_next_bday = time_to_next_bday(birthday)

print ("Days until your next birthday: ", end = "")
print_days(diff_to_next_bday)
