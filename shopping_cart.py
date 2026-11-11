# Problem 2: Simple Shopping Cart

# 1. Customer's name
customer_name = input("Enter customer name: ")

# 2. Product names and prices
product1_name = input("Enter Product 1 name: ")
product1_price = float(input("Enter Price for Product 1: "))

product2_name = input("Enter Product 2 name: ")
product2_price = float(input("Enter Price for Product 2: "))

product3_name = input("Enter Product 3 name: ")
product3_price = float(input("Enter Price for Product 3: "))

# 3. Subtotal calculation
subtotal = product1_price + product2_price + product3_price

# 4. Determine discount rate
if subtotal >= 5000:
    discount_rate = 0.20
elif 3000 <= subtotal <= 4999:
    discount_rate = 0.10
elif 1000 <= subtotal <= 2999:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discount = subtotal * discount_rate
final_total = subtotal - discount

# 5. Display shopping summary using f-string
print("\n--- Shopping Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Product 1: {product1_name}")
print(f"Price: {product1_price:.0f}" if product1_price.is_integer() else f"Price: {product1_price:.2f}")
print(f"Product 2: {product2_name}")
print(f"Price: {product2_price:.0f}" if product2_price.is_integer() else f"Price: {product2_price:.2f}")
print(f"Product 3: {product3_name}")
print(f"Price: {product3_price:.0f}" if product3_price.is_integer() else f"Price: {product3_price:.2f}")
print(f"Subtotal: {subtotal:.0f}" if subtotal.is_integer() else f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.0f}" if discount.is_integer() else f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.0f}" if final_total.is_integer() else f"Final Total: {final_total:.2f}")
