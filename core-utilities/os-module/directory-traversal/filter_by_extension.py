import os 

for root,dirs,files in os.walk("test_data"):
    for file in files:
        if file.endswith(".pdf"):
            print(file)

# output is skill_assesment.pdf