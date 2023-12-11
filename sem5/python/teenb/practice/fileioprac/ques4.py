# Write a python script to delete the specified line giving the line number from the text file.

path = "ques4.txt"
lines = []
with open(path, "r") as my_file:
    lines = my_file.readlines()
deli = int(input("Enter line to be deleted "))

delline = lines.pop(deli-1)
print(f"line deleted: {delline}")

with open(path, "w") as my_file:
    my_file.writelines(lines)
    
