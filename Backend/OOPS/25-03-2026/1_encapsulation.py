#Aceess Modifiers: Public, Private, Protected
#public: Accessible from anywhere
#private: Accessible only within the class, denoted by __ (double underscore)
#protected: Accessible within the class and its subclasses, denoted by _ (single underscore)

class Library:
    # class variables:
    library_name = "Kuvempu - Public Library"
    location = "Bengaluru"
    number_of_members = 0
    number_of_books = 0
    books_collection = []
    borrowed_books = []

    def __init__(self, member, member_id):
        # instance variables
        self.member = member
        self.member_id = member_id
        self.borrowed_books = []
        self.total_borrowed = 0

    @classmethod
    def add_book(cls, book, author, genre, publisher, copies= 1):

        book = {
            "book_id": len(cls.books_collection) + 1,
            "book": book,
            "author": author,
            "genre": genre,
            "publisher": publisher,
            "available_copies": copies,
            "total_copies": copies
        }

        cls.books_collection.append(book)
        cls.number_of_books += copies

        print(f"Book Added Successfully! The Details are as follows: ")
        print(f"Book Name: {book}")
        print(f"Author: {author}")
        print(f"Genre: {genre}")
        print(f"Publisher: {publisher}")
        print(f"Available Copies: {copies}\n")

    @classmethod
    def list_books(cls):
        if not cls.books_collection:
            print("No books available in the library. Come after some time.")
            return
        
        print(f"{cls.library_name} - {cls.location}")
        print(f"{'ID': <5} {'Book Name': <30} {'Author': <20} {'Available': <10}")
        
        for book in cls.books_collection:
            print(f"{book['book_id']:<5} {book['book']:<30} {book['author']:<25} {book['available_copies']:<10}")

        print(f"Total Books in Library: {cls.number_of_books} \n")

    def lend_book(self, book_id):
        book_to_lend = None
        for book in Library.books_collection:
            if book['book_id'] == book_id:
                book_to_lend = book
                break

        if not book_to_lend:
            print(f"Book with ID {book_id} not found!")
            return False
        
        if book_to_lend['available_copies'] <= 0:
            print(f"Sorry! {book_to_lend['book']} is currently not available.")
            return False
        
        for borrowed in self.borrowed_books:
            if borrowed['book_id'] == book_id and not borrowed['returned']:
                print(f"You have already borrowed '{book_to_lend[book]}'!")
                return False
            
        book_to_lend['available_copies'] -= 1
        Library.number_of_books -= 1

        borrow_record = {
            "book_id": book_id,
            "book": book_to_lend['book'],
            "author": book_to_lend['author'],
            "borrowed_date": self._get_current_date(),
            "returned": False
        }

        self.borrowed_books.append(borrow_record)
        self.total_borrowed += 1

        Library.borrowed_books.append({
            "member": self.member,
            "book": book_to_lend['book'],
            "book_id": book_id,
            "borrowed_date": self._get_current_date()
        })

        print("Book borrowed successfully!")
        print(f"Member Name: {self.member}")
        print(f"Book: {book_to_lend['book']}")
        print(f"Author: {book_to_lend['author']}")
        print(f"Borrowed Date: {borrow_record['borrowed_date']}")
        print(f"Remaining Copies: {book_to_lend['available_copies']} \n")

    def return_book(self, book_id):
        borrowed_record = None
        for record in self.borrowed_books:
            if record['book_id'] == book_id and not record['returned']:
                borrowed_record = record
                break

        if not borrowed_record:
            print("You have not borrowed this book or it's already returned!")
            return False

        library_book = None 
        for book in Library.books_collection:
            if book['book_id'] == book_id:
                library_book = book
                break

        if library_book:
            library_book['available_copies'] += 1
            Library.number_of_books += 1

        borrowed_record['returned'] = True
        borrowed_record['returned_date'] = self._get_current_date()
        self.total_borrowed -= 1

        for record in Library.borrowed_books:
            if (record['member'] == self.member and record['book_id'] == book_id and 'returned_date' not in record):
                record['returned_date'] = self._get_current_date()

        print("Book Returned Successfully!")
        print(f"Member: {self.member}")
        print(f"Book: {borrowed_record['book']}")
        print(f"Returned Date: {borrowed_record['returned_date']}")
        
        if library_book:
            print(f"Available Copies: {library_book['available_copies']}\n")
        return True
    
    # protected method
    def _get_current_date(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
Library.add_book("Sri Ramayana Darshanam", "Kuvempu", "Mythology", "Sapna Book House", 5)
Library.add_book("Srimadh Bhagavatham", "Madhwa", "Mythology", "Geetha Book House", 8)
Library.add_book("Panchatantra", "Madhwa", "Fiction", "Kids Stories", 12)

Library.list_books()

member1 = Library("Akshay Rao", "M-001")
member2 = Library("Ajay Rao", "M-002")

member1.lend_book(1)
member2.lend_book(1)

Library.list_books()

member1.return_book(1)

Library.list_books()