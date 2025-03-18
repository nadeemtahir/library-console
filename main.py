# Personal Library Manager (Without Database)

# List to store books
library = []

# Add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    
    library.append(book)
    print("✅ Book added successfully!")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("🗑️ Book removed successfully!")
            return
    
    print("⚠️ Book not found!")

# Update a book
def update_book():
    title = input("Enter the title of the book to update: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            book["title"] = input(f"New title (Leave blank to keep '{book['title']}'): ") or book["title"]
            book["author"] = input(f"New author (Leave blank to keep '{book['author']}'): ") or book["author"]
            book["year"] = input(f"New publication year (Leave blank to keep '{book['year']}'): ") or book["year"]
            book["genre"] = input(f"New genre (Leave blank to keep '{book['genre']}'): ") or book["genre"]
            read_status = input("Have you read this book? (yes/no): ").strip().lower()
            book["read_status"] = book["read_status"] if read_status == "" else (read_status == "yes")
            print("✅ Book updated successfully!")
            return
    
    print("⚠️ Book not found!")

# Search books
def search_books():
    search_by = input("Search by (title/author/genre/year): ").strip().lower()
    search_term = input("Enter search term: ").lower()

    results = [book for book in library if str(book.get(search_by, "")).lower() == search_term]

    if results:
        for book in results:
            print(f"📘 {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
    else:
        print("⚠️ No matching books found!")

# Display all books
def display_books():
    if library:
        for book in library:
            print(f"📘 {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")
    else:
        print("📭 Your library is empty!")

# Library statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"📚 Total books: {total_books}")
    print(f"✅ Read books: {read_books}")
    print(f"📖 Unread books: {unread_books}")
    print(f"📊 Percentage read: {percentage_read:.2f}%")

# Main menu
def main():
    while True:
        print("\n📚 Personal Library Manager")
        print("1. ➕ Add Book")
        print("2. ✏️ Edit Book")
        print("3. ❌ Remove Book")
        print("4. 🔎 Search")
        print("5. 📖 View Library")
        print("6. 📊 Stats")
        print("7. 🚪 Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            display_books()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again!")

if __name__ == "__main__":
    main()
