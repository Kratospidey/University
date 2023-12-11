# Write a python script to count the number of lines from a text file which is not starting with an alphabet "T".

proper_lines = 0
filename = "ques3.txt"

with open(filename, "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        if line[0][0] != "T" and line[0][0] != "t": # assuming case insensitivty
            proper_lines += 1
        
print(proper_lines)