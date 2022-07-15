# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    number = int(input("Function: "))
    if number == 0:
        print("Bye now!")
        break
    if number == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_diary:
            my_diary.write(f"{entry}\n")
        print("Diary saved")
    if number == 2:
        print("Entries:")
        with open("diary.txt") as my_diary:
            for line in my_diary:
                line = line.strip()
                print(line)
