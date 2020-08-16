numbers = [1, 1, 1, 1, 2, 2, 3, 4]

set_item = set(numbers)  # set is list with unique item
# methods are same as list add, remove, append
# but they are unordered list so we cannot access item like list
# Doesnt support indexing

new_set = {1, 2, 6}  # defining set

# All mathematical set operations can be used in sets

first_set = set(numbers)
second_set = {4, 8, 9}

print("Union:", first_set | second_set)
print("Intersection:", first_set & second_set)
print("Difference:", first_set - second_set)
print("Symmetic Difference:", first_set ^ second_set)
