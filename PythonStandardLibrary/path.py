from pathlib import Path

Path("C:\\Program\\Microsoft")

# Use r to use single \
Path(r"C:\Program\Microsoft")

# Path oject
Path()

# Combining paths
Path() / "PathExample" / "__init__"

# Home directory
Path.home()
path = Path("PathExample/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
#path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path)
print(path.absolute())
