# Class: blueprint for creating new objects
# Object: instance of class

# Class: Human
# Objects: John, Adam, Raman
class Point:
    # By convention function should have one parameter
    # By default we pass self
    def draw(self):
        print("draw")


# Creating object of class
point = Point()
# Calling draw method
point.draw()

# check instanceof
print(isinstance(point, Point))
