
class Point:
    # Class level attribute which is shared by all instances or object like human have two eyes, two ears
    # But we can change depending upon the requirement
    default_shape = "Dot"

    # Magic method
    def __init__(self, x, y):
        # Instance level attribute like humans have different name like John, Raman etc
        self.x = x
        self.y = y

    def draw(self):
        print("Point ({} {})".format(self.x, self.y))


point = Point(1, 2)
print(point.x)
print(point.default_shape)  # Same
print("Point1: ", point.default_shape)  # Point1
point.draw()

point2 = Point(5, 6)
print("Point2: ", point2.default_shape)  # Same
point2.draw()


# If changed
Point.default_shape = "Line"
print("Point1: ", point.default_shape)  # Same
print("Point2: ", point2.default_shape)  # Same


# Also print
print("Print using class itself: ", Point.default_shape)  # Same


# Change at instance level
point.default_shape = "Rectangle"
print("Point1: ", point.default_shape)
