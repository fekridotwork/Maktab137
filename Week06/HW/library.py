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

        #approach2
        borrowed_list = ", ".join(f"{book.isbn} : {book.title}" for book in self.borrowed_books) 

        #approach1
        # pairs = []
        # for book in self.borrowed_books:
        #     pairs.append(f"{book.isbn} : {book.title}")
        # borrowed_list = ", ".join(pairs)

        return f"Member:\nName = '{self.name}'\nid = '{self.member_id}'\nEmail = '{self.email}'\nBorrowed = [{borrowed_list}]"


class StudentMember(Member):

    MAX_BORROW = 3

    def borrow_book(self, book: Book, days: int = 30):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            print("You reached StudentMember borrow-limit.")
            return
        super().borrow_book(book, days = days)

class TeacherMember(Member):

    MAX_BORROW = 5

    def borrow_book(self, book: Book, days: int = 30):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            print("You reached TeacherMember borrow-limit.")
            return
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
        print("Library data saved to file.")

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
        

    def add_book(self, book : Book):

        #approach2
        if any (b.isbn == book.isbn for b in self.books):
            print(f"Book with this ISBN : {book.isbn} already exists.")
        else:
            self.books.append(book)
            self.save()

        # approach1
        # duplicate = False
        # for b in self.books:
        #     if b.isbn == book.isbn:
        #         duplicate = True
        #         break

        # if duplicate:
        #     print(f"Book with this ISBN : {book.isbn} already exists.")
        # else:
        #     self.books.append(book)
        #     self.saving()
    
    def add_member(self, member : Member):
        if any (m.member_id == member.member_id for m in self.members):
            print(f"Member with this ID : {member.member_id} already exists.")
        else:
            self.members.append(member)
            self.save()
    
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
        self.save()

    def return_book(self, member_id: str, isbn: str):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not book:
            print("Return failed: member or book not found.")
            return
        member.return_book(book)
        self.save()
    
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
        # results = []
        # query = title.lower()
        # for book in self.books:
        #     if query in book.title.lower():
        #         results.append(book)
        # return results

    def search_member_by_name(self, name):
        return [m for m in self.members if name in m.name]
        # results = []
        # query = name.lower()
        # for member in self.members:
        #     if query in member.name.lower():
        #         results.append(member)
        # return results

    def report_counts(self):

        total = len(self.books)

        borrowed = sum(1 for b in self.books if b.is_borrowed)
        # borrowed = 0
        # for b in self.books:
        #     if b.is_borrowed:
        #         borrowed += 1

        available = total - borrowed

        print(f"Total books: {total} | Borrowed: {borrowed} | Available: {available}")

# Testing part
if __name__ == "__main__":
  
    lib = Library.load_or_make("SimpleLib")
    print(f"Library name: {lib.name}")

    print("Adding Books :")
    a = Book("a", "author1", "0001")
    b = Book("b", "author2", "0002")
    c = Book("c", "author3", "0003")

    lib.add_book(a)
    lib.add_book(b)
    lib.add_book(c)

    print("Trying to add a book with the same isbn")
    lib.add_book(Book("a-duplicate", "x", "0001"))

    lib.show_all_books()
    lib.report_counts()

    print("Adding Members :")
    matin   = StudentMember("Matin",   "S1", "matin@example.com")
    amirali = TeacherMember("Amirali", "T1", "amirali@example.com")
    zahra   = StudentMember("Zahra",   "S2", "zahra@example.com")

    lib.add_member(matin)
    lib.add_member(amirali)
    lib.add_member(zahra)
    
    print("Trying to add a new member with the same id")
    lib.add_member(StudentMember("Matin-dup", "S1", "dup@example.com"))

    lib.show_all_members()

    print("S1 borrowing a book for 7 days :")
    lib.borrow_book("S1", "0001", days=7)
    lib.show_all_books()
    lib.report_counts()

    print("S2 wants to borrow the same book :")
    lib.borrow_book("S2", "0001", days=5)

    lib.borrow_book("S1", "0002", days=10)   
    lib.borrow_book("S1", "0003", days=10)  
    lib.show_all_members()

    print("Testing borrow-limit for students : ")
    d = Book("d", "author4", "0004")
    lib.add_book(d)
    lib.borrow_book("S1", "0004", days=3)   

    e = Book("e", "author5", "0005")
    f = Book("f", "author6", "0006")
    g = Book("g", "author7", "0007")
    h = Book("h", "author8", "0008")

    lib.add_book(e)
    lib.add_book(f)
    lib.add_book(g)
    lib.add_book(h)

    lib.borrow_book("T1", "0004")  
    lib.borrow_book("T1", "0005")  
    lib.borrow_book("T1", "0006")  
    lib.borrow_book("T1", "0007") 
    lib.borrow_book("T1", "0008")  
    
    print("Testing borrow-limit for teachers")
    i = Book("i", "author9", "0009")
    lib.add_book(i)
    lib.borrow_book("T1", "0009")  

    lib.show_all_members()
    lib.report_counts()

    print("Testing to return a book which wasn't borrowed :")
    lib.return_book("S2", "0001")  

    print("After returning a book :")
    lib.return_book("S1", "0001")
    lib.show_all_books()
    lib.report_counts()

    print("Searching :")
    print("Search 'a' ->", [bk.title for bk in lib.search_book_by_title("a")])
    print("Search 'Mat' ->", [m.name for m in lib.search_member_by_name("Mat")])

    print("Showing all books and members :")
    lib.show_all_books()
    lib.show_all_members()

    print("Testing save and load")
    lib2 = Library.load()
    print(f"Loaded library name: {lib2.name}")
    lib2.show_all_books()
    lib2.show_all_members()
    lib2.report_counts()


