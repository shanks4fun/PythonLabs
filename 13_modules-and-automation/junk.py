import pathlib

# desktop = pathlib.Path("/Users/joe/Desktop")

newPath = pathlib.Path("/Users/joe/Desktop")

for filepath in newPath.iterdir():
    print(filepath)