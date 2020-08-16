# Multilevel Inheritence
class Animal:
    def eat(self):
        print("Eats")


class Bird(Animal):
    def fly(self):
        print("Flys")


class Emu(Bird):
    pass

# Emu doesnt but still it has fly method which is an issue


# Multiple Inheritence

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# class Manager(Employee, Person):
#     pass


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()


# Multi inheritence is good when different class has unique and right method

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
