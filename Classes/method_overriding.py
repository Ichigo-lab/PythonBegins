class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("Eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # Calls Animal Constructor we can change its like below
        print("Mammal Constructor")
        self.weight = 2
        # super().__init__()  # Calls Animal Constructor

    def walk(self):
        print("Walk")


tiger = Mammal()
print(tiger.weight)
print(tiger.age)
