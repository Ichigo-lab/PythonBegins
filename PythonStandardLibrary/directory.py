from pathlib import Path

path = Path("PythonStandardLibrary")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()

for p in path.iterdir():  # genrator object
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

py_files = [p for p in path.glob("*.py")]  # search particular files
# recursively search particular files
py_filess = [p for p in path.rglob("*.py")]
print(py_files)
