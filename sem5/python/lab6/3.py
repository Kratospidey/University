import numpy as np


def fahrenheit_to_celsius(F_array):
    return (F_array - 32) / 1.8


def celsius_to_fahrenheit(C_array):
    return C_array * 1.8 + 32


# Sample Data
print()
celsius_values = np.array([0, 25, 100])
fahrenheit_values = celsius_to_fahrenheit(celsius_values)
print("Celsius values:", celsius_values)
print("Converted to Fahrenheit:", fahrenheit_values)

fahrenheit_values_sample = np.array([32, 77, 212])
celsius_converted = fahrenheit_to_celsius(fahrenheit_values_sample)
print("\nFahrenheit values:", fahrenheit_values_sample)
print("Converted to Celsius:", celsius_converted)
