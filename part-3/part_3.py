my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def a_book(dict):
    return (f'A book "{dict["title"]}" was written by {dict["author"]} in {dict["year"]}. It has rating of {dict["rating"]} and {dict["pages"]} pages.')

print(a_book(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def book_title(dict):
    return (f'A title of the book is "{dict["title"]}".')

def book_rating(dict):
    return (f'A rating of the book is {dict["rating"]}.')

def book_author(dict):
    return (f'The book was written by {dict["author"]}.')

print(book_title(my_book))
print(book_rating(my_book))
print(book_author(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def add_book(**kwargs):
    my_book2 = {
        "title": kwargs['title'],
        "author": kwargs['author'],
        "year": kwargs['year'],
        "rating": kwargs['rating'],
        "pages": kwargs['pages']
    }

    return my_book2

print(add_book(title = 'Harry Potter', author = 'J.K. Rowling', year = 1991, rating = 4.8, pages = 300))

def add_key(dict, key, value):
    dict[key] = value
    return dict

print(add_key(my_book, "borrowed", True))

def is_borrowed(dict):
    if dict["borrowed"] == True:
        dict["borrowed"] = False
    else:
        dict["borrowed"] = True

is_borrowed(my_book)
print(my_book)