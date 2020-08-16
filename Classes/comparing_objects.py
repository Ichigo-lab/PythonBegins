# Pyhon has many inbuilt magic methods for comparson, arithmetic etc

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic method for comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Arithemric operations
    def __add__(self, other):
        # Simple way
        # return self.x + other.x, self.y + other.y
        # right way
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

points = Point(10, 20)
others = Point(1, 2)
print(points > others)
print(points < others)

# Prints object
print(points + others)
