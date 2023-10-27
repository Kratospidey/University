import re

filename = "./34.txt"
count = 0

with open(filename, "r") as file:
    for line in file:
        if line[0].lower() != "t" and line.strip() != "" and line.strip() != "\n":
            count += 1

print(f"Count: {count}")
