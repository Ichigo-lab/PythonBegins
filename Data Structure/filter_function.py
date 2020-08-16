items = [
    ('Product1', 13),
    ('Product2', 18),
    ('Product3', 11)
]

x = filter(lambda item: item[1] >= 12, items)
print(x)  # returns filter object
filteredlist = list(x)
print(filteredlist)

y = map(lambda x_items: x_items[1], filteredlist)
print(list(y))
