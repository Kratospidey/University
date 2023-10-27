import re

num = input("Number: ")
print("Seperated numbers: ", re.findall(r"\d{1}", num))
