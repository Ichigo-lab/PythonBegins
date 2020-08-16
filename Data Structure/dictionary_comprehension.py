# Just like list comprehension we have set and dictionary too
# tuples have generator

# List
values_list = [x * 2 for x in range(5)]
print(values_list)


# Set
values_set = {x * 2 for x in range(5)}
print(values_set)

# Dictionary
values_dict = {}
for x in range(5):
    values_dict[x] = x * 2
print(values_dict)

# Another way of above method
values_dict = {x: x * 2 for x in range(5)}
print(values_dict)
