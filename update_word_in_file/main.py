"""
A file contain a word "Donkey" multiple time. You need to write
a program which replace this word ##### by updating the same file.
"""

word = "Donkey"

with open("./update_word_in_file/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("./update_word_in_file/file.txt", "w") as f:
    content = f.write(contentNew)
