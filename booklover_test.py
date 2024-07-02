from booklover import Booklover
import unittest
import pandas as pd
import numpy as np

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        book1 = Booklover('Jeff', 'gmail', 'Adventure')
        book1.add_book('Harry Potter', 4)
        
        self.assertTrue('Harry Potter' in book1.book_list['book_name'].values)
        
    def test_2_add_book(self):
        book2 = Booklover('Jeff', 'gmail', 'Adventure')
        book2.add_book('Harry Potter', 4)
        book2.add_book('Harry Potter', 4)
        
        actual = 0
        expected = 1
        
        for i in book2.book_list['book_name']:
            if i == 'Harry Potter':
                actual += 1
        
        self.assertEqual(actual, expected)
        
    def test_3_had_read(self):
        book3 = Booklover('Jeff', 'gmail', 'Adventure')
        book3.add_book('Harry Potter', 4)
        
        self.assertTrue(book3.has_read('Harry Potter'))
    
    def test_4_has_read(self):
        book4 = Booklover('Jeff', 'gmail', 'Adventure')
        book4.add_book('Harry Potter', 4)
        
        self.assertFalse(book4.has_read('Narnia'))
    
    def test_5_num_books_read(self):
        book5 = Booklover('Jeff', 'gmail', 'Adventure')
        book5.add_book('Harry Potter', 4)
        book5.add_book('Narnia', 4)
        
        expected = 2
        
        self.assertEqual(book5.num_books_read(), expected)
    
    def test_6_fav_books(self):
        book6 = Booklover('Jeff', 'gmail', 'Adventure')
        book6.add_book('Harry Potter', 5)
        book6.add_book('Narnia', 4)
        book6.add_book('Warriors', 3)
        book6.add_book('Alice in Chains: The Untold', 2)
        
        fav6 = book6.fav_books()
        
        self.assertFalse((fav6['book_rating'] <= 3).any())
    
if __name__ == '__main__':
    unittest.main(verbosity = 3)