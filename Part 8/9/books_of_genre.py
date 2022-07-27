# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
def books_of_genre(books: list, genre: str):
    new_list = []
    for book in books:
        if book.genre == genre:
            new_list.append(book)
    return new_list
# -----------------------------
