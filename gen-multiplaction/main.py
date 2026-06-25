"""
write a program to generate multiplication of 
table of 2 to 20 and write it to the different files
place these file in folder for a 13  year old
"""

def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"./gen-multiplaction/table_{n}", "w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)