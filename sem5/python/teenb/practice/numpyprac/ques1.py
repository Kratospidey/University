# Write Python program to Create a 5 * 6 array between 10 to 1000 such that the difference between the elements are 12 and they are only even numbers. 

# Print the even rows and odd columns from the array.

import numpy as np

array = np.arange(10,1000,12)


array = array[:30]


array = array.reshape((5,6))


print(array[0::2,1::2])