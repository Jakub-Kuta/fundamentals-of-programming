###
# Class describing an e-book
#
class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def next_page(self):
        if not self.is_open:
            print('The book is closed')
        elif self.current_page < self.pages:
            self.current_page += 1

    def previous_page(self):
        if not self.is_open:
            print('The book is closed')
        elif self.current_page > 1:
            self.current_page -= 1

    def read(self, number_of_pages):
        if not self.is_open:
            print('The book is closed')
        else:
            for i in range(number_of_pages):
                self.next_page()

    def show_status(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Number of pages: {self.pages}')
        print(f'Current page: {self.current_page}')
