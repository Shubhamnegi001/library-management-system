#LIBRARY MANAGEMENT SYSTEM 


class Book: #this is class for book 
    def __init__(self,book_id,book_title,book_author):
        self.book_id = book_id
        self.title = book_title
        self.author = book_author
        self.available = True

class Person:
    def __init__(self,person_id,name):
        self.person_name = name 
        self.person_id = person_id


class Student(Person):
    def __init__(self,student_id,name):
        super().__init__(student_id,name)
        self.issued_book = []


class Library:
    def __init__(self):
        self.books = []
        self.students = []
    
    def add_book(self):
        book_id = input("Enter Book ID : ")
        title = input("Enter Book Title : ")
        author = input('Enter Book Author Name : ')

        book = Book(book_id,title,author)
        self.books.append(book)

        print("Book Added Succesfully.")
    
    def register_student(self):
        student_id = input("Enter Student ID : ")
        name = input("Enter Student Name : ")

        student = Student(student_id,name)
        self.students.append(student)

        print(" Student Added Succesfully.")

    def issue_book(self):
        student_id = input("Enter Student ID : ")
        book_id = input("Enter Book ID : ")
        
        student = next((s for s in self.students if s.person_id == student_id),None)
        book = next((b for b in self.books if b.book_id == book_id), None)
        
        if student and book:
            if book.available:
                student.issued_book.append(book)
                book.available = False 
                print("Book Issued Succesfully.")
            else:
                print("Book Not Available Right Now.")
        else: 
            print("Student and Book Not Found")
    
    def return_book(self):
        student_id = input("Enter Student ID : ")
        book_id = input("Enter Book ID : ")

        student = next((s for s in self.students if s.person_id == student_id), None)

        if student:
            book = next((b for b in student.issued_book if b.book_id == book_id), None)

            if book:
                student.issued_book.remove(book)
                book.available = True
                print("Book returned Succesfully.")
                return
        
        print("Book not found.")


    def show_book(self):
        print("AVALABLE BOOKS")

        for book in self.books:
            if book.available:
               print(f"ID : {book.book_id} ")
               print(f"Title : {book.title}")
               print(f"Author : {book.author}")



library = Library()

while True:
    print("-"*26)
    print("LIBRARY MANAGEMENT SYSTEM ")
    print("_"*26)
    print("1. Add Book.")
    print("2. Student Register.")
    print("3. Issue Book.")
    print("4. Return Book.")
    print("5. Available Books.")
    print("6. Exit.")
    print("-"*26)

    try:
        choice = int(input("Enter Choice (1/6) : "))
    except Exception:
        print("Enter Numbers.")
        continue

    if choice == 1:
        library.add_book()  
    
    elif choice == 2:
        library.register_student()
    
    elif choice == 3:
        library.issue_book()
    
    elif choice == 4:
        library.return_book()
    
    elif choice == 5:
        library.show_book()
    
    elif choice == 6:
        print("Happy Visiting.")
        break
    else:
        print("Enter Valid Choice (1/6).")