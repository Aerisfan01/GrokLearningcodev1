def sale_price(original, discount):
 return (1 - discount/100) * original_price

product_name = input("Product: ")
original_price = float(input("Original price ($): "))
discount = float(input("Discount (%): "))

final_price = sale_price(original_price, discount)

print(f"{product_name} on sale for ${final_price:.2f}.")

