class Text(str):  # This helps in extendind "str"
    def duplicate(self):
        return self + self


text = Text("PYthon")
print(text.lower())  # Has all str methods
print(text.duplicate())

# Here we are just overriding append method
class TrackableList(list):
    def append(self, object):
        print("Append Method classed")
        super().append(object)


list1 = TrackableList()
list1.append("1")
print(list1)
