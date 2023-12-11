# Write a python script to continue writing to a file until user enters choice as y and then on user input n stop writing and 
# read the file and count words in the text file those are ending with alphabet "e".

# write as long as user chooses y
# asap user chooses n, stop writing
# then read the file and count words ending with `e`

   
path = "ques2.txt"

while True:
    choice = input("Enter y for writing to a file and n for exiting")
    if choice == "y":
        with open(path, "a") as my_file:
            my_file.write(input("Enter your line "))
    elif choice == "n":
        print("Exiting")
        break
    else:
        print("Invalid input")
        
with open(path, "r") as my_file:
    lines = my_file.read()
    count = 0
    for line in lines:
        for word in line:
            if word[-1] == "e":
                count += 1
print(count)