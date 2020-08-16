letters = ['a', 'b', 'c', 'e', 'f']
matrix = [[0, 1], [2, 3]]
zeroes = [0]*5
combined = zeroes + letters
numbers = list(range(20))
chars = list("Hello World")
char_length = len(chars)  # length of list

# letters[0] = "d"  # modify list
# print(letters)
# print(letters[0:3]) # [:3]
# print(letters[:])  # [0:]
# print(letters[::2])
# print(numbers[::-1]) # reverse order

# List unpacking
numberss = [1, 2, 3]
a, b, c = numberss

alphabets = ['a', 'b', 'c', 'd', 'e']
first, second, *others = alphabets  # 1
firt, *others, last = alphabets  # 2
# print(others)

# for letter in letters:
for letter in enumerate(letters):  # Gives tuple with first element as index
    print(letter)
# print(letter[0], letter[1])  # indices letter

for index, letter in enumerate(letters):
    print(index, letter)

# adding removing item

letters.append("s")  # inserts at the end
letters.insert(2, 'x')  # desired location
print(letters)

letters.pop()  # remove last item
letters.pop(2)  # remove with index
letters.remove("e")  # remove by item itself
del letters[0:3]  # remove range of item
# letters.clear()  # remove all item
print(letters)

# find item in list
print(letters.index('f'))

# sorting
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

num = list(range(10))
print(sorted(num))
print(sorted(num, reverse=True))

# zip function
# [(1, 11), (2, 22), (3, 33)]
list1 = [1, 2, 3]
list2 = [11, 22, 33]

print(list(zip(list1, list2)))
print(list(zip(list1, list2, "abc")))
