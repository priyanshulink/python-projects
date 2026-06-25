"""
write a program to find out the line number where python is present.
"""



with open("./line_contain_python/file.txt","r") as f:
    lines = f.readlines()

Lineno = 1
for line in lines:
    if("python" in line):
        print(f"python present at line no. {Lineno}")
        break
    Lineno += 1

else: 
        print("no python is not present")
    