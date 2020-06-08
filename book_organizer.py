import datetime
from datetime import date
from datetime import timedelta
import json



book_list = []
    
reading_list = []

path = "./files/my_folder"
filename = "booklist.json"


def add_book_to_book_list(new_book):
    book_list.append(new_book)
    # f = open(path + '/' + filename, 'a')


def add_book_to_reading_list(new_book, end_date, start_date = date.today()):
    new_book.append(start_date)
    new_book.append(end_date)
    td = end_date - start_date
    pages_per_day = round(new_book[2] / td.days, 2)
    new_book.append(pages_per_day)
    reading_list.append(new_book)


def create_book():
    # To do: fix the while loop
        title = str(input("Enter a book title: "))
        author = str(input("Who wrote this book? "))
        pages = int(input("Enter number of pages in the book: "))
        print(f"'{title}' by {author} with {pages} pages.")
        input("Do you want to keep track of a new book? Enter yes or no: ") in ('yes', "YES", "YEs", "Yes", "ye", "y")


        add_book_to_book_list([title, author, pages])
    # else:
    #     add_book_to_book_list(['book1', 'author1', 1]) 
    #     add_book_to_book_list(['book2', 'author2', 2])   
    #     add_book_to_book_list(['book3', 'author3', 3])
    #     print("Okay! Goodbye!")


# def read_book_original():
#     #fix input to only ask after already starting to read one book
#     add_one = input("Do you want to start reading? ") 
#     if add_one in ('yes', 'Yes', 'y'):
#         add_one = True
#     else:
#         add_one = False
    
#     for i, book in enumerate(book_list):
#         print(f"{i + 1} {book[0]}")

#     while add_one:
#         # put this first in this function; take it out of the while loop
#         id = input("Which book do you want to read? Enter the number of the book (or 'exit' to exit): ")
        
#         if id == 'exit':
#             add_one = False
#         else:
#             end_date = (input("What day do you want to finish this book? (Enter as yyyy-mm-dd) "))
#             end_date = date.fromisoformat(end_date)
#             add_book_to_reading_list(book_list[int(id) - 1], end_date)
    

def read_book():
    # Fix this part to print from the file
    for i, book in enumerate(book_list):
        print(f"{i + 1} {book[0]}")
    # f = open(path + '/' + filename, 'r')
    # books = f.readlines()
    # print(type(books))
    # for i, book in books[0]:
    #     print(f"{i + 1} {books[0]}")

    id = input("Which book do you want to begin reading? Enter the number of the book. ")    
    end_date = input("What day do you want to finish this book? (Enter as yyyy-mm-dd) ")
    end_date = date.fromisoformat(end_date)
    add_book_to_reading_list(book_list[int(id) - 1], end_date)

def print_reading_list():
    for my_book in reading_list:
        print(f'To read {my_book[0]} by {my_book[4]}, you need to read {my_book[5]} pages every day!')


    

def main():

    with open("/".join([path, filename]), 'r') as d:
        globals()['book_list'] = json.load(d)
    
    while True:
        user_input = input("""
To add a new book to your list, press a.
To start reading a book, press r.
To update the page you're on, press p.
To exit, press x. """)
        
        if user_input == "a":
            create_book() 
        elif user_input == "r":    
            read_book()
        elif user_input == "p":
            pass
        elif user_input == "x":
            with open("/".join([path, filename]), 'w') as f:
                json.dump(book_list, f)
            break

        print_reading_list()

if __name__ == "__main__":
    main()