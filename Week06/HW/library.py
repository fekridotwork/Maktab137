from datetime import datetime, timedelta
import pickle

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

    def mark_as_borrowed(self, days = 30):
        if self.is_borrowed:
            print(f"Book '{self.title}' is already borrowed.")
            return
        self.is_borrowed = True
        self.borrowed_time = datetime.now()
        self.return_time = self.borrowed_time + timedelta(days=days)

    def mark_as_returned(self):
        if not self.is_borrowed:
            print(f"Book '{self.title}' is not borrowed.")
            return
        self.is_borrowed = False
        self.borrowed_time = None
        self.return_time = None

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
    
    def borrow_book(self, book: Book, days: int = 30):
        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
            return
        book.mark_as_borrowed(days = days)
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            print("This member did not borrow the specified book.")
            return
        self.borrowed_books.remove(book)
        book.mark_as_returned()

    def show_info(self) -> str:
        borrowed_list = ", ".join(f"{book.isbn} : {book.title}" for book in self.borrowed_books) 
        return f"Member:\nName = '{self.name}'\nid = '{self.member_id}'\nEmail = '{self.email}'\nBorrowed = [{borrowed_list}]"


class StudentMember(Member):

    MAX_BORROW = 3

    def borrow_book(self, book: Book, days: int = 30):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            raise ValueError("You reached StudentMember borrow-limit.")
        super().borrow_book(book, days = days)

class TeacherMember(Member):

    MAX_BORROW = 5
    
    def borrow_book(self, book: Book, days: int = 30):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            raise ValueError("You reached TeacherMember borrow-limit.")
        super().borrow_book(book, days = days)

class Library:

    def __init__(self, name : str):
        self.name = name
        self.books = []
        self.members = []

    # Saving with pickle
    def save(self):
        with open('library_data.pkl', "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load():
        with open('library_data.pkl', "rb") as f:
            return pickle.load(f)

    @staticmethod
    def load_or_make(name):
        try:
            return Library.load()
        except FileNotFoundError:
            print("No data file found so we create an empty library.")
            return Library(name)
        except Exception as e:
            print(f"Failed to load data bc of {e}. \nCreating empty library.")
            return Library(name)

    def saving(self):
        self.save()
        print("Library data saved to file.")


    def add_book(self, book : Book):
        if any (b.isbn == book.isbn for b in self.books):
            print(f"Book with this ISBN : {book.isbn} already exists.")
        else:
            self.books.append(book)
            self.saving()
    
    def add_member(self, member : Member):
        if any (m.member_id == member.member_id for m in self.members):
            print(f"Member with this ID : {member.member_id} already exists.")
        else:
            self.members.append(member)
            self.saving()
    
    def find_book(self, isbn: str) -> Book:
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def find_member(self, member_id: str) -> Member:
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None
    
    def borrow_book(self, member_id: str, isbn: str, days: int = 30):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            print("Borrow failed: member or book not found.")
            return
        member.borrow_book(book, days=days)
        self.saving()

    def return_book(self, member_id: str, isbn: str):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            print("Return failed: member or book not found.")
            return
        member.return_book(book)
        self.saving()
    
    def show_all_books(self):
        print(f"Books in {self.name} :")
        for b in self.books:
            print(b.display_info())

    def show_all_members(self):
        print(f"Members in {self.name} :")
        for m in self.members:
            print(m.show_info())

    def search_book_by_title(self, title):
        return [b for b in self.books if title in b.title]

    def search_member_by_name(self, name):
        return [m for m in self.members if name in m.name]

    def report_counts(self):
        total = len(self.books)
        borrowed = sum(1 for b in self.books if b.is_borrowed)
        available = total - borrowed
        print(f"Total books: {total} | Borrowed: {borrowed} | Available: {available}")

