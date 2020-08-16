items = [
    ('Product1', 13),
    ('Product2', 18),
    ('Product3', 11)
]

#prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

#filtered = list(filter(lambda item: item[1] >= 12, items))
filtered = [item for item in items if item[1] >= 12]

print(prices)
print(filtered)
