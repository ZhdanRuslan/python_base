class Book:

    def __init__(self, author_info, author_name, year, genre, *Review):
        super().__init__()
        self.author_info = author_info
        self.author_name = author_name
        self.year = year
        self.genre = genre
        self.Review = Review

    def __str__(self):
        return "[" + self.author_info + "] [" + self.author_name + "] [" + self.year + "] [" + self.genre + "] [" + str(self.Review) + "]"

    def __repr__(self):
        return  ("{}('{}' '{}' '{}' '{}' '{}')".format(self.__class__.__name__, self.author_info, self.author_name, self.year, self.genre, self.Review))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Review:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return "[" + self.description + "]"
        
    def __repr__(self):
        return  ("{}('{}')".format(self.__class__.__name__, self.description))
    


book1 = Book("Python book", "Luts", "2016", "CS")
book2 = Book("Python book","Luts","2016","CS")
print(book1)
print(book1 == book2)
book2.year = 2018
print(book1 == book2)
book3 = Book("Python book","Luts","2016","CS", "Good", "Great!")
print(book3)
review = Review("Best of the best!")
print(review)
book4 = Book("Algo", "Kormann", "1986", "science", review)
print(book4)