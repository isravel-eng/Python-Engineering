import os

for root,dirs,files in os.walk("test_data"):
    print("Root:",root)
    print("Directories:",dirs)
    print("Files:",files)

    print("-"*100)

