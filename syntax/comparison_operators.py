lang = "python 3"

if lang == "ruby":
    print("you're using ruby")
elif lang == "python 2":
    print("OMG Please upgrade!!!")
else:
    print(f"Anything else the value was {lang}")

lang = "python 2"

if lang == "ruby":
    print("you're using ruby")
elif lang == "python 2":
    print("OMG Please upgrade!!!")
else:
    print(f"Anything else the value was {lang}")

age = 20
if age >= 10:
    print("you're older than 10")
if age >= 30:
    print("you're older than 30")
if age != 30:
    print("You're not 30")

"""
Symbols
== is equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
!= not equal to
is (keyword) reference equality

is vs ==:
== is for value equality
is is for reference equality (same memory address), largely used to check if two objects are the same
can also get same result by checking id(a) == id(b). id() fetches memory address of a piece of data, function or class
"""
