from pathlib import Path
from zipfile import ZipFile

# zipFile = ZipFile("files.zip", "w")

# for path in Path("PythonStandardLibrary").rglob("*.*"):
#     zipFile.write(path)
# zipFile.close()  # if anything goes wrong, not close so use finally or with

# with ZipFile("files.zip", "w") as zipFile:
#     for path in Path("PythonStandardLibrary").rglob("*.*"):
#         zipFile.write(path)


with ZipFile("files.zip") as zipFile:
    print(zipFile.namelist())
    info = zipFile.getinfo("PythonStandardLibrary/directory.py")
    print(info.file_size)
    print(info.compress_size)
    zipFile.extractall("extract")
