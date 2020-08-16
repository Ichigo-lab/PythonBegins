from pathlib import Path
from time import ctime
path = Path("PythonStandardLibrary/ecommerce/filesworking.py")
# print(path.exists())
# path.rename("files_working.py")
# path.unlink() Deletes file

print(path.stat())

print(ctime(path.stat().st_ctime))  # human readble

# print(path.read_text())  # Reads content of file
# print(path.write_text())  # wries content in file

# import shutil for copying moving etc
