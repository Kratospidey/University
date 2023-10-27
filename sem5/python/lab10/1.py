animals = ["Cat\n", "Dog\n", "Lion\n", "Tiger\n", "Leopard\n"]

filename = "./1.txt"

with open(filename, "w") as file:
    file.writelines(animals)

with open(filename, "r") as file:
    for line in file:
        if line.strip() != "" and line.strip() != "\n":
            print(line, end="")
