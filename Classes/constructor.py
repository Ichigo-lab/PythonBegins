class Point:
    # Magic method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Point ({} {})".format(self.x, self.y))


point = Point(1, 2)
print(point.x)
point.draw()

point2 = Point(5, 6)
point2.draw()
