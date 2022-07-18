# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthday = datetime(year, month, day)
millennium = datetime(1999, 12, 31)

age = millennium - birthday

if age.days >= 0:
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")