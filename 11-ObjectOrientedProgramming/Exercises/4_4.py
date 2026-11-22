###
# Main program using the e-book
#
import ebook

# create a book
book = ebook.EBook('The Hobbit', 'J.R.R. Tolkien', 310)

# open the book
book.open_book()

# display the book status
book.show_status()

# read a few pages
book.read(5)

# display the book status
book.show_status()

# close the book
book.close_book()

# read a few pages (the book is closed)
book.read(3)
