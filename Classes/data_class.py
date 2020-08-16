from collections import namedtuple


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# point = Point(1, 2)
# other = Point(1, 2)
# print(point == other)


# Both code are doing same thing but use below code only when dealing with attribute like x,y
# They are immutatable
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
# p1.x = 10 Gives error, -> this will help creating new object p1 = Point(x=10, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
