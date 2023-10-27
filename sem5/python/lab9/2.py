import re

text = input("String: ")

print("Three character words: ", re.findall(r"\b\w{3}\b", text))
print("Four  character words: ", re.findall(r"\b\w{4}\b", text))
print("Five  character words: ", re.findall(r"\b\w{5}\b", text))
