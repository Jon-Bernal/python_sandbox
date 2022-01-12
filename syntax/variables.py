def print_types():
  # string
  name = "Jon Bernal"
  print("name: ", type(name))

  # List (array)
  groceries = ["milk", "eggs", "ice cream"]
  print("groceries", type(groceries))

  # Dictionary (Object)
  person = {
    'key': "value",
    "name": "Jon",
    "Language": "Python"
  }

  print("person.language", person['Language'])

  # Tuple  is an immutable list (Cannot be changed, can't add or delete items)
  kids = ("Ben", "Max", "Luna")
  print("Kids: ", kids)
  print("kids type: ", type(kids))

  # Set is a mutable list that automatically removes duplicates
  foods = {'pizza', 'tacos', 'ice cream', 'pizza'}
  print("foods: ", foods) # Notice pizza is only here once
  print("foods type: ", type(foods))
  
print_types()