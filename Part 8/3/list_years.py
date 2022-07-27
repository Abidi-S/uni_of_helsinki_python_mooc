# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    new_list = []
    for item in dates:
        new_list.append(item.year)
    return sorted(new_list)