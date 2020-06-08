import datetime
from datetime import date
from datetime import timedelta
import json

#make it so it reads, manipulates, and writes dictionaries

def add_book_to_reading_list(new_book, end_date, start_date = date.today()):
    new_book.append(start_date)
    new_book.append(end_date)
    td = end_date - start_date
    pages_per_day = round(new_book[2] / td.days, 2)
    new_book.append(pages_per_day)
    reading_list.append(new_book)


def create_book():
    title = str(input("Enter a book title: "))
    author = str(input("Who wrote this book? "))
    pages = int(input("Enter number of pages in the book: "))
    print(f"'{title}' by {author} with {pages} pages.")
    new_book = [title, author, pages] 
    return new_book


def read_book(book_list):
    # Fix this part to print from the file
    for i, book in enumerate(book_list):
        print(f"{i + 1} {book[0]}")

    id = input("Which book do you want to begin reading? Enter the number of the book. ")    
    end_date = input("What day do you want to finish this book? (Enter as yyyy-mm-dd) ")
    end_date = date.fromisoformat(end_date)
    new_book = book_list[int(id) - 1].copy() 
    start_date = date.today()
    new_book.append(start_date.isoformat())
    new_book.append(end_date.isoformat())
    td = end_date - start_date
    pages_per_day = round(new_book[2] / td.days, 2)
    new_book.append(pages_per_day)
    current_page = 1
    new_book.append(current_page)
    print(f'To read {new_book[0]} by {new_book[4]}, you need to read {new_book[5]} pages every day!')
    return new_book


def read_file(path, filename):
    with open("/".join([path, filename]), 'r') as d:
        book_list = json.load(d)
    return book_list

# def read_file_dummy(path, filename):
#     with open("/".join([path, filename]), 'r') as d:
#         bl = json.load(d)
#     return bl


def save_file(path, filename, book_stuff):
    with open("/".join([path, filename]), 'w') as f:
        json.dump(book_stuff, f)
    

def main():

    path = "./files/my_folder"
    filename = "book_stuff.json"

    book_stuff = read_file(path, filename)
    
    while True:
        user_input = input("""
To add a new book to your list, press a.
To start reading a book, press r.
To update the page you're on, press p.
To exit, press x. """)
        
        if user_input == "a":
            book_stuff["book_list"].append(create_book())
        elif user_input == "r":    
            book_stuff["reading_list"].append(read_book(book_stuff["book_list"]))
        elif user_input == "p":
            pass
        # make it update the current page and recalculate the pages you have to read every day
        # date.fromisoformat to change back to datetime
        elif user_input == "x":
            save_file(path, filename, book_stuff)
            break


if __name__ == "__main__":
    main()