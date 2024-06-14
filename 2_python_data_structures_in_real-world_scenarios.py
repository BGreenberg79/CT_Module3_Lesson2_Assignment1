#Task 1 Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
    while True:
        title = input("What is the title of the book you are trying to add: ").title()
        author = input("Who is the author of this book: ").title()
        book_info = (title, author)
        if book_info not in library:
            library.append(book_info)
            print(f"The book {book_info[0]} by {book_info[1]} has been added to the library")
        else:
            print("The book you are trying to add is already in the library")
        continue_loop = input("Would you like to continue to add more books (Y/N): ")
        if continue_loop.upper() == "N":
            print("Thank you for adding books to our library")
            break
        else:
            print("Previous book added, proceeding to next book.")
            continue

add_book(library)

'''
After careful consideration I decided that the core logic of my function would be if the tuple of book_info is not in the list library.
By doing this I made it possible for there to be two different books with the same title but different authors in out library, as this is permissable under US copyright law
I also ensured that our library could carry multiple works from the same author, in case we wanted to add Animal Farm but already had 1984 in the library.
The other pieces of the function included all of our code in a while loop so that the inputs for title and author could be taken within the function before being packed into the tuple of book_info.
After packing this tuple we check if that exact tuple is in the library we pass in to the function as the argument and then either append the tuple to that list and report it or say that the book is already in the library.
Then we ask if the user would like to continue and either break of proceed to add the next book. Initially my function took no arguments and just referenced the library list as global.
Ultimately I decided against that and decided to make the library the argument/parameter as it would allow future users to abandon the library we have loaded in and could then build their own if they choose to do so.
'''