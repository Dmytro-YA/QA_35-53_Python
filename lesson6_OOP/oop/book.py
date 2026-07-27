class Book:
    pass
book = Book()
book.title = "The Great Gatsby"
book.author = "Author"
book.pages = 1000

book1 = Book()
book1.title = "Idiot"
book1.author = "Author"
book1.pages = 500

print(book.title, " - ", book.author, " - ", book.pages, " pages")
print(book1.title, " - ", book1.author, " - ", book1.pages, " pages")