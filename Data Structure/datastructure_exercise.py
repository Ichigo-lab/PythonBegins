from pprint import pprint
sentence = "This is an common interview question"

char_repetition = {}
for char in sentence:
    if char in char_repetition:
        char_repetition[char] += 1
    else:
        char_repetition[char] = 1
pprint(char_repetition)

char_repetition_sorted = sorted(
    char_repetition.items(), key=lambda kv: kv[1], reverse=True)
print(char_repetition_sorted)
