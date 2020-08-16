items = [
    ('Product1', 13),
    ('Product2', 18),
    ('Product3', 11)
]


def sort_item(item):  # item is parameter
    return item[1]   # expression


items.sort(key=sort_item)  # function passed as a reference
# items.sort(key=lambda item: item[1])  # lambda parameter:expression
print(items)
