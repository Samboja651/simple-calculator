
def addition(num1:int, num2:int)->int:
    result = num1 + num2
    return result

def subtraction(num1: int, num2: int)->int:
    result = num1 - num2
    return result

def division(num1: int, num2: int):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as error:
        error = "Can't divide by zero."
        return error

def multiplication(num1: int, num2: int)-> int:
    result = num1 * num2
    return result

def exponential(num1: int, num2: int)-> int:
    result = num1 ** num2
    return result

print("Welcome.\nOperations include: +, -, *, /, **\n")

num1 = input("Enter first number: ")
while not num1.isnumeric():
    print("Error! Number must be integer.")
    num1 = input("Enter first number: ")

num2 = input("\nEnter second number: ")
while not num2.isnumeric():
    print("Error! Number must be integer.")
    num2 = input("Enter second number: ")

operations = ["+", "-", "*", "**", "/"]
operator = input("\nEnter mathematical operator: ")
while operator not in operations:
    print("Error! operator not recognized.")
    operator = input("Enter mathematical operator: ")

num1 = int(num1)
num2 = int(num2)
try:
    if operator == "+":
        ans = addition(num1, num2)
        print(ans)
    elif operator == "-":
        ans = subtraction(num1, num2)
        print(ans)
    elif operator == "*":
        ans = multiplication(num1, num2)
        print(ans)
    elif operator == "/":
        ans = division(num1, num2)
        print(f"{ans}")
    else:
        ans = exponential(num1, num2)
        print(ans)
except:
    print("oops! unknown error occured. Try again")