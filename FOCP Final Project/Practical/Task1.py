while True:
    num_pizzas_str = input("How many pizzas ordered? ")
    if not num_pizzas_str.isdigit():
        print("Please enter a valid positive integer!")
        continue

    num_pizzas = int(num_pizzas_str)
    if num_pizzas <= 0:
        print("Please enter a valid number!")
        continue

    delivery_required = input("Is delivery required? (Y/N) ").strip().upper() 
    #strip=y pachhi ko space lai ignore garnu, 
    #upper = lowercase lai convert garera read garnu
    if delivery_required not in ('Y', 'N'):
        print('Please answer "Y" or "N".')
        continue

    is_tuesday = input("Is it Tuesday? (Y/N) ").strip().upper()
    if is_tuesday not in ('Y', 'N'):
        print('Please answer "Y" or "N".')
        continue

    used_app = input("Did the customer use the app? (Y/N) ").strip().upper()
    if used_app not in ('Y', 'N'):
        print('Please answer "Y" or "N".')
        continue

    num_pizzas = int(num_pizzas)
    delivery_required = delivery_required == 'Y'
    is_tuesday = is_tuesday == 'Y'
    used_app = used_app == 'Y'

    break  # Exit the loop if input is valid

# The rest of the program remains the same
PIZZA_PRICE = 12.00
DISCOUNT_TUESDAY = 0.5
DISCOUNT_APP = 0.25
DELIVERY_FEE = 2.50
MIN_DELIVERY_ORDER = 5

total_price = num_pizzas * PIZZA_PRICE

if delivery_required:
    if num_pizzas < MIN_DELIVERY_ORDER:
        total_price += DELIVERY_FEE
    else:
        total_price += 0.00

if is_tuesday:
    total_price *= (1 - DISCOUNT_TUESDAY)

if used_app:
    total_price *= (1 - DISCOUNT_APP)


print("\nBPP Pizza Price Calculator")
print("==========================\n")
print(f"How many pizzas ordered? {num_pizzas}")
print(f"Is delivery required? {'Y' if delivery_required else 'N'}")
print(f"Is it Tuesday? {'Y' if is_tuesday else 'N'}")
print(f"Did the customer use the app? {'Y' if used_app else 'N'}\n")
print(f"Total Price: £{total_price:.2f}.")

