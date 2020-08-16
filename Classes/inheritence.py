class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")


# Animal: Parent, Base
# Mammal: Child, SubClass

class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish:
    def swim(self):
        print("Swim")


tiger = Mammal()
tiger.eat()
print(tiger.age)
print(isinstance(tiger, Animal))


# Object class is the base class of all class in python
# class Animal(object):
# All magic methods are inherited from object class
print(isinstance(tiger, object))
print(issubclass(tiger, object))
