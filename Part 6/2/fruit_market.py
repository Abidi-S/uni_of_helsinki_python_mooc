# write your solution here
def read_fruits():
    fruit_dict = {}
    with open("fruits.csv") as fruit_file:
        for line in fruit_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit_name = parts[0]
            fruit_price = float(parts[1])
            fruit_dict[fruit_name] = fruit_price
    return fruit_dict
