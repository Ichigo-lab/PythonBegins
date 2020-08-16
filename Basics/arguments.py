# Default common

def increment(number, by):
    return number + by


print(increment(2, 1))

# Keyword argument


def increments(number, by):
    return number + by


print(increments(2, by=1))

# Default argument


def incremens(number, by=2):
    return number + by


print(incremens(2, by=1))
print(incremens(2))


# *args multiple arguments

def multiply(*numbers):
    total = 1
    print(type(numbers))
    for num in numbers:
        print(num)
        total *= num
    return total


print(multiply(2, 8, 9, 7))

# **args multiple arguments


def details(**user_details):
    print(user_details)


details(id=1, name="Arif Khan", age=24)
