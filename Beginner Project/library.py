class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def disp_info(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}'
    
class BookManagement:
    def __init__(self):
        self.books = {}
    
    def add_book(self, title, author, ISBN):
        if ISBN not in self.books:
            self.books[ISBN] = Book(title, author, ISBN)
            return "The book has been added."        
        return "The book already exists."
    
    def search_book(self, ISBN):
        if ISBN in self.books:
            book = self.books[ISBN]
            return f'The book with ISBN {book.ISBN} is {book.title} and author name is {book.author}.'
        return f"The book with ISBN {ISBN} is not found."
    
    def display_books(self):
        if self.books == []:
            return "The list of books is empty."
        return [bk.disp_info() for bk in self.books.values()]

if __name__ == '__main__':
    bks = BookManagement()
    print("Welcome to the LIBRARY.")
    while True:
        print('''\n What would you like to do ?
              To add a book --> 1
              To search a book --> 2
              To display the list of books --> 3
              To exit --> 4''')
        choice = int(input("Enter your choice:"))

        match choice:

            case 1:
                title = input("Enter the title of the book:")
                author = input("Enter the author of the book:")
                ISBN_num = int(input("Enter the ISBN number:"))
                print(bks.add_book(title,author,ISBN_num))
            case 2:
                ISBN_num = int(input("Enter the ISBN number:"))
                print(bks.search_book(ISBN_num))
            case 3:
                print(bks.display_books())
            case 4:
                print("Bye")
                break
