# They are immutable
tuple1 = (1, 2, 5)  # defining tuple
tuple2 = 6, 8, 9    # () are not mandatory
tuple3 = tuple1 + tuple2  # Concatenate
tuple4 = (1, 2) * 3  # repeats same value in tuple

list_item = [1, 2, 5, 8, 9]
tuple5 = tuple(list_item)  # convets list into tuple
char_tuple = tuple("Hello World")
print(char_tuple)

point = (1, 2, 3)
x, y, z = point

# Swapping variable

x = 10
y = 11

x, y = y, x   # y,x is basically a tuple and we are just unpacking x,y = 11,10
# as defined on line 3
