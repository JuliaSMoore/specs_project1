### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def add_book():
#     title = input("Book title: ")
#     author = input("Author: ")
#     year = input("Publishing year: ")
#     rating = input("Rating: ")
#     pages = input("Number of pages: ")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def add_book():
#     title = input("Book title: ")
#     author = input("Author: ")
#     year = int(input("Publishing year: "))
#     rating = float(input("Rating: "))
#     pages = int(input("Number of pages: "))


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def add_book():
#     title = str(input("Book title: "))
#     author = str(input("Author: "))
#     try:
#         year = int(input("Publishing year: "))
#     except:
#         year = int(input("A number is required: "))
#     try:
#         rating = float(input("Rating: "))
#     except:
#         rating = float(input("A number is required: "))
#     try:
#         pages = int(input("Number of pages: "))
#     except: 
#         pages = int(input("A number is required: "))

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu():

#     process = True

#     try:
#         choice = int(input('1 - List of All Books \n 2 - Add a Book \n 3 - Quit App'))
#     except: choice = int(input("Please, enter a number: "))

#     if choice == 1:
#         print_books(book_list)
#     elif choice == 2:
#         book_list.append(add_book())
#     elif choice == 3:
#         print('Quitting')
#         process = False
#     else:
#         print("Please, enter a number between 1 and 3")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

book_list = []

def add_book(book_list):
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

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    book_list.append(new_book)


def print_books(book_list):

    for book in book_list:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title} \n Author: {author} \n Year: {year} \n Rating: {rating} \n Pages: {pages}")


def main_menu(book_list):

    process = True

    while process:
        try:
            choice = int(input('1 - List of All Books \n 2 - Add a Book \n 3 - Quit App \n'))
        except: choice = int(input("Please, enter a number: "))

        if choice == 1:
            print_books(book_list)
        elif choice == 2:
            add_book(book_list)
        elif choice == 3:
            print('Quitting')
            process = False
        else:
            print("Please, enter a number between 1 and 3")

main_menu(book_list)
