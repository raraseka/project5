print("Welcome to the Trip Cost Calculator!")
days=int(input("How many days will you stay?"))
hotel_price=float(input("How much does hotel cost per night?$"))
flight_price=float(input("How much does flight cost?$"))
rental_car=float(input("If you need rental car please enter the price otherwise enter zero.$"))
other_expenses=float(input("Enter other possible expenses $"))
total_cost=round(days * hotel_price + flight_price + days * rental_car + other_expenses, 2)
print(f"Total cost:  ${total_cost}")




