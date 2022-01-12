def indexing():
    # String indexes
    course = "Python 3 Crash Course"
    print(course[9:14]) # prints "Crash"

    # Lists and tuples
    groceries = ["milk", "eggs", "ice cream"]
    # Prints all groceries after 0th index
    print("groceries[1:]", groceries[1:]) 
    # print foods from start of list to index 1
    print("groceries[:1]", groceries[:1]) 

    # Tuples are essentially the same as lists
    kids = ("Ben", "Max", "Luna")
    print("Kids[:2]: ", kids[:2])

indexing()