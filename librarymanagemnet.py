class Book:

    def __init__(self, book_id, author, title, quantity):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.quantity = quantity
        self.available_quantity = quantity

    def display(self):
        print(
            "Book ID:",
            self.book_id,
            "Author:",
            self.author,
            "Title:",
            self.title,
            "Total Quantity:",
            self.quantity,
            "Available Quantity:",
            self.available_quantity,
        )

class Library:

    def __init__(self):
        self.books = []

    def add_book(self):

        while True:
            book_id = int(input("Enter the book ID: "))

            if book_id > 0:
                break
            else:
                print("Invalid ID! Enter a positive number.")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        author = input("Enter the author: ")
        title = input("Enter the title: ")

        while True:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                break
            else:
                print("Invalid quantity! Enter a positive number.")

        new_book = Book(book_id, author, title, quantity)
        self.books.append(new_book)

        print("Book added successfully!")

    def view_books(self):

        if not self.books:
            print("Books unavailable")
        else:
            for book in self.books:
                book.display()

    def search_book_by_id(self):

        while True:
            search_id = int(input("Enter book ID: "))

            if search_id > 0:
                break
            else:
                print("Invalid ID! Enter a positive number.")

        found = False

        for book in self.books:
            if book.book_id == search_id:
                book.display()
                found = True
                break

        if not found:
            print("Book not found")

    def search_book_by_title(self):

        search_title = input("Enter book title: ")
        found = False

        for book in self.books:
            if book.title.lower() == search_title.lower():
                book.display()
                found = True

        if not found:
            print("Book not found")

    def issue_book(self):

        while True:
            book_id = int(input("Enter the book ID you want to issue: "))

            if book_id > 0:
                break
            else:
                print("Invalid ID! Enter a positive number.")

        found = False

        for book in self.books:
            if book.book_id == book_id:
                found = True

                if book.available_quantity > 0:
                    book.available_quantity -= 1
                    print("Book issued successfully!")
                else:
                    print("No books available")

                break

        if not found:
            print("Book not found")

    def return_book(self):

        while True:
            book_id = int(input("Enter the book ID you want to return: "))

            if book_id > 0:
                break
            else:
                print("Invalid ID! Enter a positive number.")

        found = False

        for book in self.books:
            if book.book_id == book_id:
                found = True

                if book.available_quantity < book.quantity:
                    book.available_quantity += 1
                    print("Book returned successfully!")
                else:
                    print("Book already returned")

                break

        if not found:
            print("Book not found")



library = Library()



book1 = Book(102, "Alex Michaelides", "The Silent Patient", 10)
book2 = Book(103, "Jane Austen", "Pride and Prejudice", 6)
book3 = Book(105, "Khaled Hosseini", "The Kite Runner", 8)



library.books.append(book1)
library.books.append(book2)
library.books.append(book3)


choice = 0

while choice != 7:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book by ID")
    print("4. Search Book by Title")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        library.search_book_by_id()

    elif choice == 4:
        library.search_book_by_title()

    elif choice == 5:
        library.issue_book()

    elif choice == 6:
        library.return_book()

    elif choice == 7:
        print("Thank you for using the Library Management System!")

    else:
        print("Invalid choice! Please try again.")
