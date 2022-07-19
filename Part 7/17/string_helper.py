# Write your solution here
def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        capital = char.upper()
        if char == capital:
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string

def split_in_half(orig_string: str):
    string_length = len(orig_string)
    p1 = orig_string[0:int(string_length//2)]
    p2 = orig_string[string_length//2:string_length]
    return (p1), (p2)

def remove_special_characters(orig_string: str):
    is_valid_char = "abcdefghijklmnopqrstuvwxyz1234567890 "
    new_string = ""
    for char in orig_string:
        lower_char = char.lower()
        if lower_char in is_valid_char:
            new_string += char
    return new_string


if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    split_str = "abcd"
    p1, p2 = split_in_half(split_str)

    print(p1)
    print(p2)
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))