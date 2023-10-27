import numpy as np

# Generate an array of even numbers between 10 and 1000 with a step size of 12
array = np.arange(10, 1000, 12)
# Filtering only even numbers
even_array = array[array % 2 == 0]

# Reshape to 5x6 matrix
matrix = even_array[:30].reshape(5, 6)


print()
print("Generated 5x6 Matrix:")
print(matrix)

# Print even rows and odd columns
result = matrix[1::2, ::2]
print("\nEven Rows and Odd Columns:")
print(result)
