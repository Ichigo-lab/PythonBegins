# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value


# product = Product(50)
# print(product.get_price())

# Above code is unpythonic

# One way to implemnet property
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(50)
print(product.price)


# Best way to implement property
class Products:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


products = Products(100)
print(products.price)

# if we comment setter, it will become readyonly means we can set only once
# Try commentting
products.price = 2
print(products.price)
