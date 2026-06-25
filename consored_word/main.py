words = ["Donkey","bad","gande"]

with open("./consored_word/file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("./consored_word/file.txt", "w") as f:
    content = f.write(content)

