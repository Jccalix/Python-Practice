operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = float(num1) + float(num2)
elif operator == "-":
    result = float(num1) - float(num2)
elif operator == "*":
    result = float(num1) * float(num2)
elif operator == "/":
    result = float(num1) / float(num2)
else:
    result = "Invalid operator"

print("The result is:", result)