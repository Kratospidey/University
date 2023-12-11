# Write a factorial function and raise a ValueError with a custom message if input isnt integer or is negative
import math
def fact(num):
    if not (isinstance(num, int)):
        raise ValueError("Factorial must be of an integer!")
    elif num < 0:
        raise ValueError("Factorial can not be negative!")
    else:
        return (math.factorial(num))
        
    
def main():
    val = int(input("Enter a number ")) 
    # val = "a" # to test int value error
    print(fact(val))

if __name__ == "__main__":
    main()