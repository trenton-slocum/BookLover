import pandas as pd
import numpy as np

class Booklover():
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        if not isinstance(rating, int):
            raise TypeError('Rating must be an integer')
            
        if 0 > rating or rating > 5:
            raise ValueError('Rating must be in between 0 and 5')
            
        if any(book_name in book for book in self.book_list['book_name']):
            print('This book is already on the list!')
        
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
        
            
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
        
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list.loc[self.book_list['book_rating'] > 3]