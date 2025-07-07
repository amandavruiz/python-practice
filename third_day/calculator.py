def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: division by zero!"
    else:
        return "Invalid operator!"

def get_number(message):
    user_input = input(message).replace(',', '.')
    try:
        return float(user_input)
    except ValueError:
        print("Error: invalid value!")
        return get_number(message)  

num1 = get_number("Enter the first number: ")
operator = input("Enter the operator (+, -, *, /): ")
num2 = get_number("Enter the second number: ")

result = calculate(num1, operator, num2)

print(f"The result is: {result}")