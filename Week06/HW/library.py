class Book:
    total_books = 0
    def __init__(self, title : str, author : str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        Book.total_books += 1
    def mark_as_borrowed():
        pass
    def mark_as_returned():
        pass
    def display_info(self) -> str :
        if self.is_borrowed :
            status = "Borrowed"
        else:
            status = "Available"
        return f"Book :\nTitle = '{self.title}' \nAuthor = '{self.author}'\nisbn = '{self.isbn}'\nstatus = {status}"

b = Book("Clean Code", "Robert C. Martin", "9780132350884")
print(b.display_info())
print("Total:", Book.total_books)
