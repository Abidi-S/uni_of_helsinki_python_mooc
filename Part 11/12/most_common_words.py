# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            words += line.split()
    words = [word.strip(".,!-—()\n ") for word in words]
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

# rewrite this hot garbage