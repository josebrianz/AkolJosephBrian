
# Console-Based E-Commerce Checkout Program

print(" ")
print("   E-COMMERCE CHECKOUT SYSTEM")
print(" ")

# User credentials
users = {
    "Admin": "admin123",
    "Customer": "cust123",
    "Cashier": "cash123"
}

# Login System
attempts = 3
logged_in = False

while attempts > 0:
    print("\n LOGIN ")
    role = input("Enter role (Admin/Customer/Cashier): ")
    password = input("Enter password: ")

    if role in users:
        if password == users[role]:
            print(f"\nLogin successful! Welcome, {role}.")
            logged_in = True
            break
        else:
            attempts -= 1
            print("Incorrect password.")
            print("Attempts remaining:", attempts)
    else:
        attempts -= 1
        print("Invalid role.")
        print("Attempts remaining:", attempts)

if not logged_in:
    print("\nToo many failed attempts. Access denied.")
    exit()

# Role-Based Access
if role == "Admin":
    print("Admin privileges granted.")
elif role == "Customer":
    print("Customer privileges granted.")
elif role == "Cashier":
    print("Cashier privileges granted.")

print("\n CHECKOUT ")

# Get subtotal
subtotal = float(input("Enter purchase subtotal: $"))

# Coupon validation
coupon = input("Enter coupon code (or press Enter if none): ")

coupon_discount = 0

if coupon != "":
    if coupon == "SAVE10":
        coupon_discount = 10
        print("Valid coupon: 10% discount applied.")
    elif coupon == "SAVE20":
        coupon_discount = 20
        print("Valid coupon: 20% discount applied.")
    else:
        print("Invalid coupon code. No coupon discount applied.")
else:
    print("No coupon used.")

# Tiered discounts using nested conditions
tier_discount = 0

if subtotal >= 500:
    tier_discount = 15
elif subtotal >= 300:
    tier_discount = 10
elif subtotal >= 100:
    tier_discount = 5
else:
    tier_discount = 0

print(f"Tier discount: {tier_discount}%")

# Apply tier discount first
discounted_total = subtotal - (subtotal * tier_discount / 100)

# Apply coupon discount
discounted_total = discounted_total - (
    discounted_total * coupon_discount / 100
)

# Tax calculation based on location
location = input("Enter location (Local/Regional/International): ")

if location.lower() == "local":
    tax_rate = 5
elif location.lower() == "regional":
    tax_rate = 10
elif location.lower() == "international":
    tax_rate = 15
else:
    tax_rate = 8
    print("Unknown location. Default tax rate of 8% applied.")

# Apply tax
tax_amount = discounted_total * tax_rate / 100
final_price = discounted_total + tax_amount

# Display receipt
print("\n RECEIPT ")
print(f"User Role: {role}")
print(f"Original Subtotal: ${subtotal:.2f}")
print(f"Tier Discount: {tier_discount}%")
print(f"Coupon Discount: {coupon_discount}%")
print(f"Subtotal After Discounts: ${discounted_total:.2f}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"FINAL PRICE: ${final_price:.2f}")
print(" ")

print("\nThank you for shopping with us!")
