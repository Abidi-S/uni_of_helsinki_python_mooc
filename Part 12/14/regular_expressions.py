# Write your solution here
# rwrite everything using is not none rip rip
import re
def is_dotw(my_string: str):
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for days in week:
        if re.search(days, my_string):
            return True
    return False

def all_vowels(my_string: str):
    if re.search("^[aeiouy]+$", my_string):
        return True
    return False

def time_of_day(my_string: str):
    valid_hour = "^([0-1][0-9]|2[0-3]):"
    valid_minute = "([0-5][0-9]):"
    valid_second = "([0-5][0-9])$"
    valid_time = valid_hour + valid_minute + valid_second
    print (valid_time)
    if re.search(valid_time, my_string):
        return True
    return False
