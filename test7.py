library = {}

def add_book():
    book_info = input("Enter the title, genre, and price of the book (separated by |): ")
    try:
        title, genre, price = book_info.split('|')
        price = float(price)  # Ensure the price is stored as a float
        library[title] = (genre, price)
        print(f"Added {title} to the library.")
        return True
    except ValueError:
        print("Error: Please enter the information in the correct format: 'Title|Genre|Price'")
        return False

    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here

def remove_book():
    title = input("Enter the title of the book to remove: ")
    if title in library:
        del library[title]
        print(f"Removed {title} from the library.")
        return True
    else:
        print(f"Error: {title} not found in the library.")
        return False
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here

def get_book_info():
    title = input("Enter the title of the book: ")
    if title in library:
        genre, price = library[title]
        print(f"Title: {title}\nGenre: {genre}\nPrice: ${price:.2f}")
    else:
        print(f"Error: {title} not found in the library.")
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here

def list_books():
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    genre = input("Enter the genre to search for: ")
    found_books = {title: (g, p) for title, (g, p) in library.items() if g.lower() == genre.lower()}
    
    if not found_books:
        print(f"\nNo books found in the {genre} genre.\n")
        return False
    
    print()
    for title, (g, p) in sorted(found_books.items()):
        print(f"{title} ({g},${p:.2f})")
    print()
    return True
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

