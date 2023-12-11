# Read two integers number from the user using int(input0) and handle the following exceptions:
# - ValueError - Occurs when input value is not an integer.
# - ZeroDivisionError - Occurs when divisor is zero.
# - Exception - Any other error.

while True:
    try:
        num1 = int(input("Enter the first number "))
        num2 = int(input("Enter the second number "))
        print(f"{num1/num2:.3f}")
        break
    except ValueError:
        print("Error!")
        print("Please enter a proper number!")
    except ZeroDivisionError:
        print("Error!")
        print("Division by zero is not possible!")
        
    except Exception as e:
        print()
        print(f"Error Occured {e}")