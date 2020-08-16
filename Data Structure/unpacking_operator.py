numbers = [1, 2, 3]
print(numbers)
# we can use * which directly spreads
print(*numbers)


values = list(range(5))
print(values)
# spread values
print(*range(5), *"Hello")

# spread in the list
valuess = [*range(5), *"Hello"]
print(valuess)
print(*valuess)


# spread dictionary
first = {"x": 1}
second = {"y": 4, "z": 3}
combined = {**first, **second, "v": 4}
print(combined)
