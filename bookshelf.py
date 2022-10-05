from dbm.ndbm import library
from typing import KeysView


class Library:

    def __init__(self) -> None:
        self.shelf ={}

    def add_book(self,book_name, book_rating):
        if book_name not in self.shelf():
            book = {}
            book[book_name] = book_rating
            self.shelf[book_name] = book
            print('book not available')
        else:
            print(f'book {book_name} is currently in the library, with rating{self.shelf.get(book_name)}')

    def change_book_rating(self,book_name, new_rating):
        if book_name not in self.shelf.keys():
            print(f'Book {book_name} not here check market or add it here')
        else:
            book = self.shelf.get(book_name)
            book[book_name] = new_rating
            print(f'book rating updated to {new_rating}')

    def get_all_books(self):
        print(self.shelf)

    def delete_book(self,book_name):
        if book_name in self.shelf.keys():
            self.shelf.pop (book_name)
            print(f'we have removed {book_name} from library')
        else:
            print('on a norms the book isn\'t here')
    
    def get_book_by_book_name(self, book_name):
        if book_name in self.shelf.Keys():
            print(self.shelf.get(book_name))
        else:
            print (f'book{book_name} does not exist here')
    
    def get_books_with_same_ratings(self, book_rating):
        books = self.shelf.values()
        book_same_rating = {}
        for book in books:
            if book_rating in book.values():
                book_same_rating.get(book)
                if book_same_rating =={}:
                    print (f'Books not found')
                else:
                    print (book_same_rating)



library = library()
library.add_book('Me and you', 10)
library.add_book('Ada is a girl', 5.5)
library.add_book('Fullness of God', 10.0)
library.add_book('God\'s not dead', 10.0)

print(library.get_book_by_book_name('fullness of God'))
