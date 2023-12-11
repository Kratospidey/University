# Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit  degrees and vice versa. 

# Values are stored into a NumPy array.

import numpy as np

def convert_to_celsius(arr):
    return (arr - 32) * 5/9

def convert_to_fahrenheit(arr):
    return (arr * 9/5) + 32


cels = np.array([0,25,100])
print(convert_to_fahrenheit(cels))
fars = np.array([32,77,212])
print(convert_to_celsius(fars))