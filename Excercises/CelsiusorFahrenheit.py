unit = input("Celsius or Fahrenheit? (C or F)")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {temp} F")
elif unit == "F":
    temp = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {temp} C")
else:
    print(f"{unit} is not a valid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
