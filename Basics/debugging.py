def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print("Start")
print(multiply(1, 2, 3))
