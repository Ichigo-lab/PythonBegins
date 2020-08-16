items = [
    ('Product1', 13),
    ('Product2', 18),
    ('Product3', 11)
]

prices = []

# for item in items:
#     prices.append(item[1])

# print(prices)

x = map(lambda item: item[1], items)  # returns map object
print(x)  # we can iterate using loop
print(list(x))  # make a list
