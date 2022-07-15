# Write your solution here
def read_input(string, x, y):
    while True:
        try:
            n = int(input(string))
            if n in range(x, y):
                return n
        except ValueError:
            pass
        print(f"You must type in an integer between {x} and {y}")