def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
def get_operator():
    print("\nwhat operation do you want?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("enter 1, 2, 3, or 4:")
    return choice

keep_going = True


while keep_going:
    # Get numbers from user
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    # Get operation from user
    operator = get_operator()

    # Do the calculation
    if operator == "1":
        result = add(num1, num2)
    elif operator == "2":
        result = subtract(num1, num2)
    elif operator == "3":
        result = multiply(num1, num2)
    elif operator == "4":
        result = divide(num1, num2)
    else:
        print("Invalid operation selected.")
        continue

    print("\nResult:", result)

    again = input("\nDo you want to do another calculation? (yes/no): ")
    if again.lower() != "yes":
        keep_going = False 
        print("Thank you for using the calculator!")