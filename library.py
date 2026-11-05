library = {
    "PYTHON BASICS": "Available",
    "CLEAN CODE": "Available",
    "ARTIFICIAL INTELLIGENCE": "Available",
    "PYTHON PROJECTS": "Available"
}

print("--- Welcome to Our Library! ---")
print("Here are the available books:")
for book, status in library.items():
    print(f"- {book}: {status}")

while True:
    action = input("\nDo you want to (borrow) a book, (return) a book, or (exit)? ").lower()
    
    if action == "exit":
        print("Thank you for visiting our library!")
        break
    elif action == "borrow":
        book_name = input("Enter the book name you want to borrow: ").upper()
        if book_name in library:
            if library[book_name] == "Available":
                library[book_name] = "Borrowed"
                print(f"You have successfully borrowed '{book_name}'.")
            else:
                print(f"Sorry, '{book_name}' is already borrowed.")
        else:
            print("Sorry, this book is not in our library.")
            
    elif action == "return":
        book_name = input("Enter the book name you want to return: ").upper()
        if book_name in library:
            if library[book_name] == "Borrowed":
                library[book_name] = "Available"
                print(f"Thank you! You have successfully returned '{book_name}'.")
            else:
                print(f"This book was not borrowed.")
        else:
            print("This book does not belong to our library.")
