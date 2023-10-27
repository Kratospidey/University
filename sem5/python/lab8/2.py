add = lambda x: x + 26
multiply = lambda x, y: x * y

a = int(input("A: "))
print(f"{a} + 26 = {add(a)}", end="\n\n")

a = int(input("A: "))
b = int(input("B: "))


print(f"{a} x {b} = {multiply(a, b)}")
