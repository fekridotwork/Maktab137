class Book:
    total_books = 0
    def __init__(self, title : str, author : str, isbn: str):
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

# b = Book("Clean Code", "Robert C. Martin", "9780132350884")
# print(b.display_info())
# print("Total:", Book.total_books)

class Member:
    def __init__(self, name : str, member_id : str, email : str):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books = []
    
    def borrow_book(self, book: Book):
        if book.is_borrowed:
            #raise ValueError(f"Book '{book.title}' is already borrowed.")
            print(f"Book '{book.title}' is already borrowed.")
        else:    
            book.is_borrowed = True
            self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            #raise ValueError("This member did not borrow the specified book.")
            print("This member did not borrow the specified book.")
        else:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def show_info(self) -> str:
        borrowed_list = ", ".join(f"{book.isbn} : {book.title}" for book in self.borrowed_books) 
        return f"Member:\nName = '{self.name}'\nid = '{self.member_id}'\nEmail = '{self.email}'\nBorrowed = [{borrowed_list}]"

#Testing
# m = Member("Matin", "1234", "fekridotwork@gmail.com")
# b1 = Book("CLRS", "Unknown", "9780132350")
# b2 = Book("ClRS2", "Unknown", "9781491943")

# m.borrow_book(b1)
# print(f"After borrowing b1:\n{b1.display_info()}")
# print(m.show_info())

# m.borrow_book(b1)

# m.return_book(b1)
# print(f"After returning b1:\n{b1.display_info()}")
# print(m.show_info())

# m.return_book(b2)

class StudentMember(Member):
    MAX_BORROW = 3
    
    def borrow_book(self, book : Book):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            raise ValueError("You reached StudentMember borrow-limit.")
        super().borrow_book(book)

class TeacherMember(Member):
    MAX_BORROW = 5

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            raise ValueError("You reached TeacherMember borrow-limit.")
        super().borrow_book(book)

# #Testing
# books = [
#     Book("B1", "A", "I1"),
#     Book("B2", "A", "I2"),
#     Book("B3", "A", "I3"),
#     Book("B4", "A", "I4"),
#     Book("B5", "A", "I5"),
#     Book("B6", "A", "I6"),
# ]

# stu = StudentMember("Ali", "S100", "ali@example.com")
# stu.borrow_book(books[0])
# stu.borrow_book(books[1])
# stu.borrow_book(books[2])
# print("Student after 3 borrows:", stu.show_info())

# try:
#     stu.borrow_book(books[3])
# except Exception as e:
#     print("Expected (student limit):", e)

# tch = TeacherMember("Maryam", "T200", "maryam@example.com")
# tch.borrow_book(books[3])
# tch.borrow_book(books[4])
# tch.borrow_book(books[5])

# b7 = Book("B7", "A", "I7")
# b8 = Book("B8", "A", "I8")
# tch.borrow_book(b7)
# tch.borrow_book(b8)
# print("Teacher after 5 borrows:", tch.show_info())

# b9 = Book("B9", "A", "I9")
# try:
#     tch.borrow_book(b9)
# except Exception as e:
#     print("Expected (teacher limit):", e)

class Library:

    def __init__(self, name : str):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book : Book):
        if any (b.isbn == book.isbn for b in self.books):
            print(f"Book with this ISBN : {book.isbn} already exists.")
        else:
            self.books.append(book)
    
    def add_member(self, member : Member):
        if any (m.member_id == member.member_id for m in self.members):
            print(f"Member with this ID : {member.member_id} already exists.")
        else:
            self.members.append(member)
    
    def find_book(self, isbn: str) -> Book:
        for b in self.books:
            if b.isbn == isbn:
                return b
        print("Book not found.")

    def find_member(self, member_id: str) -> Member:
        for m in self.members:
            if m.member_id == member_id:
                return m
        print("Member not found.")

    def borrow_book(self, member_id: str, isbn: str):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        member.borrow_book(book)

    def return_book(self, member_id: str, isbn: str):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        member.return_book(book)
    
    def show_all_books(self):
        print(f"Books in {self.name} :")
        for b in self.books:
            print(b.display_info())

    def show_all_members(self):
        print(f"Members in {self.name} :")
        for m in self.members:
            print(m.show_info())

