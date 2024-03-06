def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    return final_price

# Prompt the user to enter the original price of an item
price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage (as a percentage): "))

# Calculate the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount, or if no discount was applied, print the original price
if final_price == price:
    print("No discount was applied. The original price is: ", price)
else:
    print("The final price after applying the discount is: ", final_price)