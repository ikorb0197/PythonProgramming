class Book:
    total_books = 0 # Total number of books created

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    # I want to create a method which will work with total books
    # Class method
    @classmethod
    def reset_total_books(cls):
        """Reset the total book count to zero"""
        cls.total_books = 0
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["title"], data["author"], data["year"])
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
book1 = Book("Python 101", "J. Doe", 2023)
data = {"title": "Learning Python", "author": "John Smith", "year": 2020}
book2 = Book.from_dict(data)

print(book1)
print(book2)