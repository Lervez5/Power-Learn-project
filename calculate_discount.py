""" Here is the function that calculates the discount """
def calculate_discount(price, discount_percent):
    # Checks if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Returns the original price if discount is less than 20%
        return price

# Prompts the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculates and prints the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying the discount is: ${final_price:.2f}")
