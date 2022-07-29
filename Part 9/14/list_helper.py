# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        occurences = 0
        most_common = ""
        for item in my_list:
            count = my_list.count(item)
            if count > occurences:
                occurences = count
                most_common = item
        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        unique = []
        for item in my_list:
            if my_list.count(item) >= 2 and item not in unique:
                unique.append(item)
        return len(unique)
