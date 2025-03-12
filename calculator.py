# Calculator
import math
import random

# Define the functions
def add_num(n1, n2):
    return n1 + n2

def sub_num(n1, n2):
    return n1 - n2

def mul_num(n1, n2):
    return n1 * n2

def div_num(n1, n2):
    if n2 == 0:
        return "Division by zero is not allowed"
    return n1 / n2



def calculations():
    print("Simple Calculator")

calculations()

# Take user inputs
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

operations = {
    "+": add_num,
    "-": sub_num, 
    "*": mul_num,
    "/": div_num
}

# Print available operations
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick any symbol from above: ")

if operation_symbol not in operations:
    print("Invalid operation symbol!")
else:
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {first_answer}")

    # Continue or stop
    should_continue = True

    while should_continue:
        other = input("Do you want to continue with the answer? Type 'y' for yes or 'n' for no: ")
        
        if other == 'y':
            operation_symbol = input("Enter another symbol: ")
            if operation_symbol not in operations:
                print("Invalid operation symbol!")
                continue
            n3 = float(input("Enter next number: "))
            calculation_function = operations[operation_symbol]
            first_answer = calculation_function(first_answer, n3)
            print(f"{first_answer}")
        
        elif other == 'n':
            should_continue = False
            print(f"Final result: {first_answer}")
        else:
            print("Invalid input. Please type 'y' or 'n'.")


