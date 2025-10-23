from datetime import datetime, timedelta

class Book:
    total_books = 0
    def __init__(self, title : str, author : str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_time = None 
        self.return_time = None
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
        if self.is_borrowed and self.borrowed_time and self.return_time:
            time_status = f"Borrowed at {self.borrowed_time:%d/%m} -> Due {self.return_time:%d/%m}"
        else:
            time_status = ""
        return f"Book :\nTitle = '{self.title}' \nAuthor = '{self.author}'\nisbn = '{self.isbn}'\nstatus = {status} | {time_status}"

class Member:
    def __init__(self, name : str, member_id : str, email : str):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.borrowed_books = []
    
    def borrow_book(self, book: Book):
        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:    
            book.is_borrowed = True
            book.borrowed_time = datetime.now()                 
            book.return_time = book.borrowed_time + timedelta(days=30) 
            self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            print("This member did not borrow the specified book.")
        else:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            book.borrowed_at = None    
            book.due_at = None 

    def show_info(self) -> str:
        borrowed_list = ", ".join(f"{book.isbn} : {book.title}" for book in self.borrowed_books) 
        return f"Member:\nName = '{self.name}'\nid = '{self.member_id}'\nEmail = '{self.email}'\nBorrowed = [{borrowed_list}]"


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

