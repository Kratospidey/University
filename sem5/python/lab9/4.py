import re

text = input("String: ")
print("String with colons: ", re.sub(r"\.|,|\s", ":", text))

