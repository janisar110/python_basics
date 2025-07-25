# list , tuple , dictionries

# list
# list changeable
# # python allow multiple data types values
# list1 = ["Test",2,True,None]
# print(list1)

# # python allow duplicate values in list
# list2 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list2)

# # list item change (checking its changeable or not)
# users2 = ["Jansiar","Salman","Faaiz"]
# users2[2] = "Fayyaz"
# print(users2)

# # Access items from list
# users = ["Jansiar","Salman","Faaiz"]
# print(users[2])


# # access last element or access from last index values using index in minus -1, -2
# thislist5 = ["apple", "banana", "cherry"]
# print(thislist5[-1])


# # range index values
# thislist6 = ["apple", "banana", "cherry","a", "b","c"]
# print(thislist6[-3:-1])

# # check item is exists or not
# thislist = ["apple", "banana", "cherry"]
# myInput = input("Check your fruit is available: ")
# if myInput in thislist:
#   print("Yes, 'apple' is in the fruits list")




# list methods add, remove, update, read

# Book library list
library = []

def show_menu():
    print("\n===== Book Library Menu =====")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Update Book Title")
    print("4. View All Books")
    print("5. Exit")

condition = True

# inifinty loop
while condition:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # Add a book
    if choice == "1":
        book = input("Enter the name of the book to add: ")
        library.append(book)
        print(f"✅ '{book}' has been added to the library.")

    # Remove a book
    elif choice == "2":
        book = input("Enter the name of the book to remove: ")
        if book in library:
            library.remove(book)
            print(f"🗑️ '{book}' has been removed.")
        else:
            print(f"⚠️'{book}' not found in the library.")

    # Update book title
    elif choice == "3":
        old_name = input("Enter the current book name: ")
        if old_name in library:
            new_name = input("Enter the new book name: ")
            index = library.index(old_name)
            library[index] = new_name
            print(f"🔄 '{old_name}' updated to '{new_name}'.")
        else:
            print(f"⚠️ '{old_name}' not found to update.")

    # view books
    elif choice == "4":
        if library:
            print("\n📚 Books in Library:")
            for idx, book in enumerate(library, start=1):
                print(f"{idx}. {book}")
            search = input("Search book here: ")
            for idx, book in enumerate(library, start=1):
                if search == book:
                    print(f"'{search}' is founded at '{idx}'!") 
                    break                
        else:
            print("📭 No books in the library.")
    # Exit
    elif choice == "5":
        print("👋 Exiting the library. Goodbye!")
        condition = False
    else:
        print("❌ Invalid choice. Please select from 1 to 5.")




# # Tuple
# # tuple unchangeable
# tuple1 = ("Test",2,True, None)
# print(tuple1)

# # Same works as list 
# Allow duplicates values
# Multiple data types can be stored

# # tuple item unchange (checking its unchangeable or not)
# users2 = ("Jansiar","Salman","Faaiz")
# users2[2] = "Fayyaz"
# print(users2)










# thislist = ["apple", "banana", "cherry"]
# copyList = thislist.copy()
# copyList2 = thislist.copy()
# thislist[1] = "blackcurrant"
# print(thislist)
# print(copyList)
