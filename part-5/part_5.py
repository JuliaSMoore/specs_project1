from pprint import pprint

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def add_book():
    title = str(input("Book title: "))
    author = str(input("Author: "))
    try:
        year = int(input("Publishing year: "))
    except:
        year = int(input("A number is required: "))
    try:
        rating = float(input("Rating: "))
    except:
        rating = float(input("A number is required: "))
    try:
        pages = int(input("Number of pages: "))
    except: 
        pages = int(input("A number is required: "))

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# add_book()
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def get_books():
    books = []
    with open("library.txt", "r") as f:
       library = f.readlines()


    for book in library:
        title, author, year, rating, pages = book.split(", ")
        books.append({
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
                })
    return books


def print_books(books):
    for book in books:
        print(f'Title: {book["title"]} \nAuthor: {book["author"]} \nYear: {book["year"]} \nRating: {book["rating"]} \nPages: {book["pages"]}\n')
    


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def pages_sum(books):
    sum = 0
    for book in books:
        sum = sum + int(book["pages"])
    print(sum)

def get_authors(books):
    for book in books:
        print(book["author"])

def get_titles(books):
    for book in books:
        print(book["title"])


def main_menu():

    process = True

    while process:
        try:
            choice = int(input('1 - List of All Books \n2 - Add a Book \n3 - Get Authors \n4 - Get Titles \n5 - Get Pages \n6 - Quit\n'))
        except: choice = int(input("Please, enter a number: "))

        if choice == 1:
            print_books(get_books())
        elif choice == 2:
            add_book()
        elif choice == 3:
            get_authors(get_books())
        elif choice == 4:
            get_titles(get_books())
        elif choice == 5:
            pages_sum(get_books())
        elif choice == 6:
            print('Quitting')
            process = False
        else:
            print("Please, enter a number between 1 and 3")

if __name__ == "__main__":
    main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

