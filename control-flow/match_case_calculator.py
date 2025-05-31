num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case '+':
        print(f"The result is: {num1 + num2}")
    case '-':
        print(f"The result is: {num1 - num2}")
    case '*':
        print(f"The result is: {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Cannot divide by zero..")
    