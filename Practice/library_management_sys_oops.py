class Book:
    def __init__(self, book_name, aut_name, book_id):
        self.book_name = book_name
        self.aut_name = aut_name
        self.availability = 1
        self.book_id = book_id

class Member:
    def __init__(self, mem_name, mem_id):
        self.mem_name = mem_name
        self.mem_id = mem_id
        self.books_borrowed = []

class Library:
    def __init__(self):
        self.list_books = []
        self.list_members = []

    def add_book(self, obj_book):
        self.list_books.append(obj_book)

    def add_mem(self, obj_mem):
        self.list_members.append(obj_mem)

    def issue_book(self, obj_mem, obj_book):
        if obj_book in self.list_books:
            if obj_mem in self.list_members:
                if obj_book.availability == 1:
                    obj_book.availability = -1
                    obj_mem.books_borrowed.append(obj_book)
                    print("Book issued successfully")
                else:
                    print("The book is not available")
            else:
                print("The member does not exist")
        else:
            print("The book does not exist in the library")

    def return_book(self, obj_mem, obj_book):
        if obj_mem in self.list_members:
            if obj_book in obj_mem.books_borrowed:
                obj_mem.books_borrowed.remove(obj_book)
                print("Book returned successfully ")
                obj_book.availability = 1
                return
            else:
                print("The book was not borrowed")
        else:
            print("The member does not exist")

    def display_avai(self):
        for book in self.list_books:
            if book.availability == 1:
                print(f"{book.book_name} : {book.aut_name}")

    def borrowed_books(self, obj_mem):
        for book in obj_mem.books_borrowed:
            print(f"{book.book_name} : {book.aut_name} : {book.book_id}")

book1 = Book("Harry Potter", "J.K. Rowling", 101)
book2 = Book("Atomic Habits", "James Clear", 102)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 103)
book4 = Book("1984", "George Orwell", 104)

member1 = Member("Dhruv", 1)
member2 = Member("Aryan", 2)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.add_mem(member1)
library.add_mem(member2)

print("===== AVAILABLE BOOKS =====")
library.display_avai()

library.issue_book(member1, book1)
library.issue_book(member1, book2)
library.issue_book(member2, book3)

print("\n===== AVAILABLE BOOKS AFTER ISSUING =====")
library.display_avai()

print("\n===== Dhruv's BORROWED BOOKS =====")
library.borrowed_books(member1)

print("\n===== ARYAN'S BORROWED BOOKS =====")
library.borrowed_books(member2)

print("\n===== TRY TO ISSUE ALREADY ISSUED BOOK =====")
library.issue_book(member2, book1)

print("\n===== RETURN BOOK =====")
library.return_book(member1, book1)

print("\n===== AVAILABLE BOOKS AFTER RETURN =====")
library.display_avai()

print("\n===== Dhruv's BOOKS AFTER RETURN =====")
library.borrowed_books(member1)

print("\n===== TRY TO RETURN BOOK NOT BORROWED =====")
library.return_book(member1, book3)

print("\n===== TRY NON-EXISTENT MEMBER =====")
fake_member = Member("Rahul", 99)
library.issue_book(fake_member, book4)

print("\n===== TRY NON-EXISTENT BOOK =====")
fake_book = Book("Dune", "Frank Herbert", 105)
library.issue_book(member1, fake_book)