class Library:

    def __init__(self):
        self.book_list = []
        self.search_list = []

    def create_book(self, title, author, date):
        book_dict = {'title': title, 'author': author, 'date': date, 'available': True}
        self.book_list.append(book_dict)

    def new_book(self, title, author, date):
        self.create_book(title, author, date)
        return self.book_list[-1]

    def get_books(self):
        return self.book_list

    def loan_book(self, title, author, date):
        for book in self.book_list:
            if book['title'] == title and book['author'] == author and book['date'] == date:
                book['available'] = False

    def return_book(self, title, author, date):
        for book in self.book_list:
            if book['title'] == title and book['author'] == author and book['date'] == date:
                book['available'] = True

    def search_library(self, title):
        self.search_list = []
        for books in self.book_list:
            if books['title'] == title:
                self.search_list.append(books)
        self.search_list.sort(key=lambda book: book.get("date"), reverse=True)
        return self.search_list

lms = Library()
lms.create_book('Harry Potter', 'J. K. Rowling', 1997)
lms.create_book('Harry Potter', 'J. K. Rowling', 1999)
lms.create_book('Harry Potter', 'J. K. Rowling', 2003)
lms.create_book('The Art of War', 'Sun Dzi', 2000)
lms.loan_book('Harry Potter', 'J. K. Rowling', 1999)
print(lms.new_book('Rich Dad Poor Dad', 'Robert Kiyosaki', 2010))
print(lms.get_books())
lms.return_book('Harry Potter', 'J. K. Rowling', 1999)
print(lms.get_books())
print(lms.search_library('Harry Potter'))