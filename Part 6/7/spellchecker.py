# write your solution here
string = input("Write text: ")



dictionary = []
with open("wordlist.txt") as word_list:
    for line in word_list:
        dict_word = line.strip()
        dictionary.append(dict_word)

for words in string:
    words = string.split(" ")

sentence = ""
for word in words:
    if word.lower() not in dictionary:
        index = words.index(word)
        word = "*" + word + "*"
        words[index] = word
    sentence += word + " "

print(sentence)