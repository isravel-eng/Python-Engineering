import os 

items = os.listdir()

for item in items:

    if os.path.isfile(item):
        print(f"{item} is a FILE")
    
    elif os.path.isdir(item):
        print(f"{item} is a FOLDER")

