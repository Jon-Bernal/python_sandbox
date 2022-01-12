# Tons of ways to format strings

"""
There are a bunch of ways to format strings in python.
the oldest way is with %s for %string, see first example
the second old way is to use "string {} var2 here {}".format(var1, var2)
The newer better way is with f strings like so print(f"stuff {var1}, etc")
"""
name = "Python"
print("Hello %s" % "World")
course = "{} for Everybody".format(name)
print("course: ", course)
print(f"f strings course name: {name} for everybody")