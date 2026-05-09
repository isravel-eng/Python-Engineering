# `os` Module
### What is `os` Module?
> The os module allows Python to interact with the operating system.

It gives Python access to :

-  files
- folders
- paths
- environmental variables 
- process/system operations
---
### Why `os` Module Matters
without `os`:
> Python only works inside memory

with `os`:
> Python can interact with the actual computer

This is the foundation of :

- automation
- scripting
- backend systems
- DevOps
- tooling
- data engineering
---
### Importing
```py
import os
```
#### Core Access of `os`
| Area| Purpose|
|----------|---------|
| Directory handling | Create/access folders|
|File handling| Manage files|
|Path handling|Work safely with paths|
|Traversal|Scan directories|
Environment variables| System configurations
Process interaction| Run/manage processes
---
#### 1. Current Working Directory
`os.getcwd`

Returns current working directory

Example:
```py
import os
print(os.getcwd())
```
Output example:
```
C:\Python\Python-Engineering
```
#### 2. Change Directory
`os.chdir()`

Changes current folder

Example
```py
os.chdir("test_folder")
```
#### 3. List Directory Contents 
`os.listdir()`

Returns files and folders.

Example 
```py
print(os.listdir())
```

Example Output
```
['a.txt','images','main.py']
```
##### Used for:
- file scanning
- automation 
- batch processing

#### 4. Create folder
`os.mkdir`

Creates single folder.

Example 
```py
os.mkdir("demo")
```
#### 5. Create Nested Folders
`os.makedirs()`

Create multiple folders recursively.

Example 
```py
os.makedirs("a/b/c")
```

#### 6. Remove Folder
`os.rmdir`

Removes empty folder.

Example
```py
os.rmdir("demo")
```
#### 7. Rename File/Folder
`os.rename()`

Example
```py
os.rename("old.txt","new.txt")
```
#### 8. Delete File 
`os.remove()`

Example
```py
os.remove("data.txt")
```
#### 9. Path handling 
`os.path.join()`

Example
```py
path = os.path.join("folder","file.txt")
```
Output
```
folder\file.txt
```

#### 10. Check Path Exists 
`os.path.exists()`

Example
```py
os.path.exists("demo")
```
Output
```py
True
False
```
#### 11.  Check File 
`os.path.isfile()`

Example
```py
os.path.isfile("s.txt")
```

#### 12. Check Directory
`os.path.isdir()`

Example
```py
os.path.isdir()
```
#### 13. File Size 
`os.path.getsize()`

Example
```py
os.path.getsize("movie.mp4")
```

Output
```
1048576
```
#### 14. Absolute Path
`os.path.abspath()`

Example
```py
os.path.abspath("main.py")
```
Output
```
C:\Python\Python-Engineering\main.py
```
#### 15. Recursive Directory Traversal 
`os.walk()`

Example
```py
for root,dirs,files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
```
Returns 
| Variable | Meaning |
| -------- | ------- |
root | current folder 
dirs | subfolders 
files | files

Used in 
- backup systems
- search engines 
- antivirus 
- dataset scanning
- automation tools

#### 16. Environment Variables
`os.getenv()`

Gets system environment variable.
Example 
```py
print(os.getenv("PATH"))
```
#### Set Environment Variable 
```py
os.environ["MODE"]="DEV"
```
Used for:

- API keys 
- DB URLs 
- deployment configs

#### 17. Process Information 
Process Id
```py
os.getpid()
```
Operating system name
```py
os.name
```
windows - nt



