import re

with open("input/raw-text.txt", "r") as file:

    text = file.read()
print(text)


emails = re.findall("[a-z0-9.]+@[a-z0-9.]+", text)
print(emails)