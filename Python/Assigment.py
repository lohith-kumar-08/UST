
# 1).

def calculate(total_kilometers,liters_per_kilometer,price_per_liter):
    
    total_liters = total_kilometers * liters_per_kilometer

    total_cost = total_liters * price_per_liter

    print(f"The total cost of the trip is: {total_cost:.2f}")


total_kilometers = float(input("Enter the total kilometers to travel"))
liters_per_kilometer = float(input("Enter the liters-per-kilometer"))
price_per_liter = float(input("Enter the price of fuel per liter"))

calculate(total_kilometers,liters_per_kilometer,price_per_liter)



# 2).

def total_expenses(quantity, price_per_item):
    total_cost = quantity * price_per_item

    if quantity > 10:
        discount = total_cost * 0.10
        total_cost -= discount

    return total_cost

quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))

total_expenses = total_expenses(quantity, price_per_item)

print(f"The total expenses are: {total_expenses:.2f}")
