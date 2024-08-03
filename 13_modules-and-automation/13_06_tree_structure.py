# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib

rootFolder = pathlib.Path("/Users/joe/Desktop/codingnomads")



for item in rootFolder.iterdir():
    if item.is_dir():
        for py_file in item.iterdir():
            if py_file.suffix == ".py":
                print(py_file)
