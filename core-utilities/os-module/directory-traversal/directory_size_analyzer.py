import os

dirs = os.listdir("test_data")
d_dirssize = {}
root_dir="test_data"

for d in dirs:
    folder_path = os.path.join(root_dir,d)
    if os.path.isdir(folder_path):
        total_size = 0
        for root,dirs,files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root,file)
                total_size+= os.path.getsize(full_path)
        d_dirssize[d] = total_size

for d,size in d_dirssize.items():
    print(f"{d} : {(size/(1024**2)):.5f} mb")