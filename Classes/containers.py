class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        #self.tags[tag] = self.tags.get(tag, 0) + 1
        # Handles case sensitive
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.tags[tag.lower()] = value

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("python")
cloud.add("oggy")

cloud["python"] = 10

for tag in cloud:
    print(tag)
