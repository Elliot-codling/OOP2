#oop in python

class Book:
    def __init__(self, title, auther, isbn):
        self.title = title
        self.auther = auther
        self.isbn = isbn
        self.available = True

    def lend(self):
        if self.available:
            self.available = False
            print(f"The book {self.title} has been borrowed")
        else:
            print(f"The book {self.title} cannot be borrowed")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book {self.title} has been returned")
        else:
            print(f"The book {self.title} cannot be returned")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Auther: {self.auther}")
        print(f"Isbn: {self.isbn}")
        if self.available:
            print(f"Available: Yes")
        else:
            print(f"Available: No")
# Define current books
book1 = Book("Harry potter and the goblet of fire", "JK Rowling", 42)
books = [book1]

# Search options
def search_book():
    title = ""
    auther = ""
    available = ""
    print("Search by:")
    print("(1) Title")
    print("(2) Auther")
    print("(3) Availablility")
    print("")
    options = input(">>>")

    if options == "1":
        title = input("Enter title: ").lower()
    elif options == "2":
        auther = input("Enter auther: ").lower()
    elif options == "3":
        print("(1) Yes")
        print("(2) No")
        print("")
        available = input("Enter option: ")

    else:
        print("Error, Invalid option")

    found = False
    for book in books:
        if book.title.lower() == title:
            print("Found!")
            print(f"Its isbn number is: {book.isbn}")
            found = True
            break

        if book.auther.lower() == auther:
            print("Found!")
            print(f"Its isbn number is: {book.isbn}")
            found = True
            break

    if not found:
        print("No book found")

    if available == "1":
        for book in books:
            if book.available:
                print(f"Title: {book.title}")
                print(f"Auther: {book.auther}")
                print(f"Isbn: {book.isbn}")
                print("")
                print("")
    
def find_book(isbn):
    for book in books:
        if book.isbn == isbn:
            return book
        
    print("No book found!")

# Main game loop
run = True
while run:
    # Find a book by its isbn number
    print("Welcome to Elliots pop up book shop!")
    print("(1) Lend book")
    print("(2) Return book")
    print("(3) Display Details of book")
    print("(4) List books")
    print("(5) Search Book")
    print("(6) Quit Program")
    print("")
    options = input(">>> ")
 
    if options == "1":
        isbn = int(input("Enter isbn Number: "))  
        book = find_book(isbn)
        if book != None:
            book.lend()
        print("")
        
    elif options == "2":
        isbn = int(input("Enter isbn Number: "))
        book = find_book(isbn)
        if book != None:
            book.return_book()
        print("")
        
    elif options == "3":
        isbn = int(input("Enter isbn Number: "))
        book = find_book(isbn)
        if book != None:
            book.display_details()
        print("")
        
    elif options == "4":
        for book in books:
            book.display_details()
            print("")
        
    elif options == "5":
        search_book()
        print("")
    elif options == "6":
        run = False
    else:
        print("Error, Invalid option")
    
    