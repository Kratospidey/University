import re

text = input("String: ")
print("String without whitespace: ", re.sub(r"\s", "", text))
