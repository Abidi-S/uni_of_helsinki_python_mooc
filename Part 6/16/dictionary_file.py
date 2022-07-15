# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    number = int(input("Function: "))

    if number == 3:
        print("Bye!")
        break
    if number == 1:
        fin_word = input("The word in Finnish: ")
        eng_word = input("The word in English: ")
        with open("dictionary.txt", "a") as dict_file:
            dict_file.write(f"{fin_word};{eng_word}\n")
        print("Dictionary entry added")
    if number == 2:
        search_str = input("Search term: ")
        rel_dict = []
        with open("dictionary.txt") as dict_file:
            for line in dict_file:
                line = line.strip()
                parts = line.split(";")
                for i in parts:
                    if search_str in i:
                        rel_dict.append(parts)

        for entry in rel_dict:
            print(f"{entry[0]} - {entry[1]}")
