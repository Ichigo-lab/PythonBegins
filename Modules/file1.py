from packageFolder.subPackageFolder import sub_package_example
from packageFolder import package_example
print("File1 Initialized")
# Import pack_example


def calc_tax():
    print("Tax")


def calc_shipping():
    print("Shipping")


package_example.pack()

sub_package_example.sub_pack()

# list of method in dir
# print(dir(package_example))
print(package_example.__name__)
