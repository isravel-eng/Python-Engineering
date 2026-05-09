import os 

total_files=total_images=total_texts=total_python_files=total_pdf=total_docx=total_videos=0

for root,dirs,files in os.walk("test_data"):
    for file in files:
        total_files+=1

        if file.endswith(".jpg") or file.endswith(".webp"):
            total_images+=1
        elif file.endswith(".txt"):
            total_texts+=1
        elif file.endswith(".py"):
            total_python_files+=1
        elif file.endswith(".pdf"):
            total_pdf+=1
        elif file.endswith(".docx"):
            total_docx+=1
        elif file.endswith(".mp4"):
            total_videos+=1

print("Total number of file is",total_files)
print("Total number of pdf is",total_pdf)
print("Total number of images is",total_images)
print("Total number of text files is",total_texts)
print("Total number of docx is",total_docx) 
print("Total number of videos is",total_videos)
