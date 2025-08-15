weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K or L)").strip().lower()

if unit == "k":
    weight = weight * 2.20462
    unit = "Lbs"
    print(f"Weight is: {weight} {unit}")
elif unit == "l":
    weight = weight / 2.20462
    unit = "Kgs"
    print(f"Weight is: {weight} {unit}")
else:
    print(f"{unit} is not a valid unit. Please use 'K' for Kilograms or 'L' for Pounds.")


