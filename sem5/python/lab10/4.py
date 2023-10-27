filename = "./34.txt"

lines = []

with open(filename, "r") as file:    
    lines = file.readlines()
    print(len(lines))

with open(filename, "w") as file:
    while True:
        del_line = int(input("Enter line number for deletion: "))

        if del_line >= 1 and del_line <= len(lines):
            break
        else:
            print("Invalid line number")

    line = lines[del_line - 1]
    del lines[del_line - 1]

    file.writelines(lines)

    print(f"Deleted '{line}' from {filename}")