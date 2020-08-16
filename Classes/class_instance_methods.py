class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Class level method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print("Point ({} {})".format(self.x, self.y))


# we have class method for the same reason as class attribute
point = Point.zero()  # works point = Point(0, 0)
point.draw()

point2 = Point(1, 2)
p = point2.zero()
p.draw()
point2.draw()
