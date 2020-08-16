from sys import getsizeof


# Doesnt stores in memory
values = (x * 2 for x in range(5))
print(values)
for val in values:
    print(val)


# Lets see how generator is useful

values_list = [x * 2 for x in range(100)]
values_gen = (x * 2 for x in range(100))
print("Gen:", getsizeof(values_gen), "List:", getsizeof(values_list))

values_lists = [x * 2 for x in range(10000)]
values_gens = (x * 2 for x in range(10000))
print("Gen:", getsizeof(values_gens), "List:", getsizeof(values_lists))

# Generator doesnt stores value in memory
# Gives on iteration basis
# such as len cannot be used here
