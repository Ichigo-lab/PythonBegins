try:
    amount = int(input("Amount: "))
# except ValueError:
#     print("You didn't enter a valid age.")
except ValueError as ex:
    print("Please enter number: ", ex)
    print(type(ex))
else:
    # This line executed when no errors were thrown
    print("No exceptions were thrown.")

# Different exception
try:
    age = int(input("Age: "))
    xfactor = 10 / age
# except (ValueError, ZeroDivisionError):  # Can we multiple exception in one line
#     print("You didn't enter a valid age.")
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exceptions were thrown.")
finally:
    print("This block will always be executed whether exception is thrown or not.")

# we can use with statement instead of finally but only for those methods which has enter and exit class
# like file 
