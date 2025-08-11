item = input("Enter the item you want to add to the cart: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total_price = price * quantity

print(f"Total price for {quantity} of {item} is: ${total_price:.2f}")