# write your solution here

def largest():
    items = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            items.append(int(line))
    return max(items)