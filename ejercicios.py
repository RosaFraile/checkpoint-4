import math
from decimal import Decimal

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

# List
students = ["Rodrigo", "Ester", "Laura", "Fernando", "Alicia"]

# Tuple
teachers = ("Gonzalo", "Teresa", "Rafael")

# Float
float_number = 245.34

# Integer
integer_number = 5

# Decimal
decimal_number = Decimal(45.23)

# Dictionary
family_tree = {
  "grand parents": {
     "paternal": ["Manuel", "Gracia"],
     "maternal": ["Ricardo", "Marina"]
  },
  "parents": ["Angel", "Yolanda"],
  "children": ["Enrique", "Isabel","Teresa"]
}

# Exercise 2: Round your float up.
number_one = math.ceil(float_number)

# Exercise 3: Get the square root of your float
number_two = math.sqrt(float_number)

# Exercise 4: Select the first element from your dictionary.
grand_parents = family_tree["grand parents"]

# Exercise 5: Select the second element from your tuple.
second_element = teachers[1]

# Exercise 6: Add an element to the end of your list.
students.append("Julio")

# Exercise 7: Replace the first element in your list.
students[0] = "Armando"

# Exercise 8: Sort your list alphabetically.
students.sort()

# Exercise 9: Use reassignment to add an element to your tuple.
teachers += ("Vanesa",)
