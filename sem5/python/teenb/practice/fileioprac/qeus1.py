# Write a list of lines into a file using writelines() and then to print non-empty lines of the file one at a time.

path = r"ques1.txt"

lines = ["Param is gay", "Jash is gay", "Adi is a minor", ""]

new_lines = [line + "\n" for line in lines]

with open(path, "w") as my_file:
    my_file.writelines(new_lines)

with open(path, "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        if line != "":
            print("###")
            print(line, end="")
            print("###")
        

