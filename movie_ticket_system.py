
# Step 1: Get inputs
day = input("Day (weekday/weekend): ").lower()
customer = input("Type (regular/student/senior): ").lower()
time = int(input("Showtime hour (9-22): "))
tickets = int(input('Number of tickets: '))


# Step 2: Base price calculations
if day == "weekend":
    price = 300
else:
    price = 200
base price = price

if customer == "student":
    price = price * 0.80  # 20% off
elif customer == "senior":
    price = price * 0.70  # 30% off

if time < 12:
    price = price * 0.90

if tickets > 5 :
    price = price * 0.95

print(f"Final ticket price: {price:.2f}")
    
    
