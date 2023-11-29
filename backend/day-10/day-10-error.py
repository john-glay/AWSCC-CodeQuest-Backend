# def divide(a, b):
#     return a / b

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a second number: "))
#     quotient = divide(a, b)
# except Exception as e:
#     print(f"Invalid input: {e}")
# else:
#     print(f"The quotient is {quotient}")

def divide(a, b):
    return a / b

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    quotient = divide(a, b)
except ValueError as ve:
    print(f"Invalid input. Please enter valid integers: {ve}")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero second number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The quotient is {quotient}")