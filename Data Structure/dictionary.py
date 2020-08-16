person_details = {"Age": 56, "Name": "Obama"}  # key should be immutable
person_details1 = dict(Age=75, Name="Trump")

# Updating value using key
person_details["Age"] = 59
# Adding new value
person_details1["Position"] = "USA President"
print(person_details1)
# Accessible using key not index
print(person_details["Age"])
# but this gives error when value is there
# print(person_details["Agee"])  # Gives error
# If not present returns None
print(person_details.get("Agee"))

# Deletes entry
del person_details1["Position"]
print(person_details1)

# Looping dictionary value
for key in person_details:
    print(key, person_details[key])

for details in person_details.items():  # Gives tuple so we can unpack as
    # for key, value in person_details.items():
    print(details)
