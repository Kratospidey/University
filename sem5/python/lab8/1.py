a = 0
b = 1

fib_nums = []

for i in range(10):
    fib_nums.append(a)
    a, b = b, a + b

fib_sq = list(map(lambda x: x**2, fib_nums))

print(fib_nums)
print(fib_sq)
