import os 
file_count=0

for root,dirs,files in os.walk("test_data"):
    for file in files:
        file_count+=1

print(f"Total number of files in 'test_data' is {file_count}")

# output is Total number of files in 'test_data' is 10