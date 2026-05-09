import os

d_filesize={}

for root,dirs,files in os.walk("test_data"):
    for file in files:
        full_path = os.path.join(root,file)
        d_filesize[file]=os.path.getsize(full_path)

largest_file = max(d_filesize,key=d_filesize.get)
size = d_filesize[largest_file]
print("largest file is",largest_file)
print("size in bytes is",size)
print("size in mb",size / (1024**2))