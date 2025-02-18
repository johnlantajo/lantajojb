class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.year_published}"


def add_book(books, title, author, year_published):
    books.append(Book(title, author, year_published))


def edit_book(book, title=None, author=None, year_published=None):
    if title:
        book.title = title
    if author:
        book.author = author
    if year_published:
        book.year_published = year_published


books = [
    Book("The Jungle Book", "Rudyard Kipling", 1894),
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960)
]


for book in books:
    print(book.describe())


edit_book(books[0], year_published=1895)  


add_book(books, "Brave New World", "Aldous Huxley", 1932)


print("\nUpdated Book List:")
for book in books:
    print(book.describe())
