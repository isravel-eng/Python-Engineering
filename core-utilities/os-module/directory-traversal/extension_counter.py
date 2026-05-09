import os

d_extension={}
for root,dirs,files in os.walk("test_data"):
    for file in files:
        if file.endswith(".txt"):
            d_extension[".txt"] = d_extension.get(".txt",0)+1
        elif file.endswith(".pdf"):
            d_extension[".pdf"] = d_extension.get(".pdf",0)+1
        elif file.endswith(".py"):
            d_extension[".py"] = d_extension.get(".py",0)+1
        elif file.endswith(".jpg"):
            d_extension[".jpg"]= d_extension.get(".jpg",0)+1
        elif file.endswith(".docx"):
            d_extension[".docx"]=d_extension.get(".docx",0)+1

for ex,count in d_extension.items():
    print(ex,":",count)