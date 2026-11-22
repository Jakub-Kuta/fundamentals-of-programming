###
# Copies the book data from a given genre to its corresponding file
#
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import csv

def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))

def copy_genre(books, genre, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        for book in books:
            if book['Genre'] == genre:
                writer.writerow(book.values())

books = read_books('books.csv')
copy_genre(books, 'Fantasy', 'books_fantasy.txt')
copy_genre(books, 'Historical', 'books_historical.txt')
copy_genre(books, 'Romance', 'books_romance.txt')
copy_genre(books, 'Classic', 'books_classic.txt')
