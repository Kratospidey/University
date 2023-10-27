import re

filename = "./2.txt"

while True:
    choice = input("Do you wish to write?[y/n]: ")[0].lower()

    if choice == "y":
        with open(filename, "a") as file:
            text = input("Text: ") + "\n"
            file.writelines(text)

    elif choice == "n":
        matches = []
        with open(filename, "r") as file:
            for line in file:
                matches.extend(re.findall(r"\b\w.*e\b", line, re.IGNORECASE))
                print(line, end="")

            print(f"Matches: {matches}")
            print(f"Count: {len(matches)}")
            exit()

    else:
        print("Invalid Choice")
