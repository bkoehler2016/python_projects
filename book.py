class Book:
    def __init__(self, name, year, author_first, author_last ):
        self.name = name
        self.year = year
        self.author = Author(author_first, author_last)
    pass

class Author:
    def __init__(self, first, last ):
        self.first = first
        self.last= last
        pass